# -*- coding: utf-8 *-*
import sys
import logging
import time

import boto.dynamodb


if sys.version_info[0] >= 3:
    unicode = str


class DynamoFormatter(logging.Formatter):
    def format(self, record):
        data = record.__dict__.copy()

        if record.args:
            msg = record.msg % record.args
        else:
            msg = record.msg
        data.update(
            args=str([unicode(arg) for arg in record.args]),
            message=str(msg),
        )

        # Remove empty keys from the dictionary
        data = dict((k, v) for k, v in data.iteritems() if v)

        if 'exc_info' in data and data['exc_info']:
            data['exc_info'] = self.formatException(data['exc_info'])

        return data


class DynamoHandler(logging.Handler):
    """ Custom log handler

    Logs all messages to a Dynamo table. This handler is designed to be used with the standard python logging mechanism.
    """

    @classmethod
    def to(cls, table_name, aws_region, aws_access_key_id, aws_secret_access_key, level=logging.NOTSET):
        """ Create a handler for a given  """
        return cls(table_name, aws_region, aws_access_key_id, aws_secret_access_key, level)

    def __init__(self, table_name, aws_region, aws_access_key_id, aws_secret_access_key, level=logging.NOTSET):
        """ Init log handler and store the table handle """
        logging.Handler.__init__(self, level)

        conn = boto.dynamodb.connect_to_region(aws_region,
                                               aws_access_key_id=aws_access_key_id,
                                               aws_secret_access_key=aws_secret_access_key)

        try:
            self.table = conn.get_table(table_name)
        except DynamoDBResponseError as e:
            table_schema = conn.create_schema(
                hash_key_name='logger_name',
                hash_key_proto_value=str,
                range_key_name='timestamp',
                range_key_proto_value=float
            )

            table = conn.create_table(
                name=table_name,
                schema=table_schema,
                read_units=10,
                write_units=10
            )

        self.formatter = DynamoFormatter()

    def emit(self, record):
        """ Store the record in the table. Async insert """
        try:

            formatted_record = self.format(record)

            item = self.table.new_item(
                # TO-DO decide what is going to be the keys of the table
                range_key=str(time.time()),  # timestamp
                hash_key=formatted_record['name'],  # name of the logger
                attrs=formatted_record
            )

            item.put()

        except Exception as e:
            logging.error("Unable to save log record: %s", e.message, exc_info=True)
