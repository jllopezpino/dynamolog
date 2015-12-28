# -*- coding: utf-8 *-*
import logging
import traceback
import sys


from dynamolog import DynamoHandler

if __name__ == '__main__':

    log = logging.getLogger('example')
    log.setLevel(logging.DEBUG)

    handler = DynamoHandler.to('table_name',
                               'dynamodb_region',
                               'dynamodb_key',
                               'dynamodb_secret')
    log.addHandler(handler)

    log.debug("1 - debug message")
    log.info("2 - info message")
    log.warn("3 - warn message")
    log.error("4 - error message")
    log.critical("5 - critical message")
    log.debug("debug message with arguments %s %s %s", 1, "2", 3)

    def log_uncaught_exceptions(ex_cls, ex, tb):
        log.critical(''.join(traceback.format_tb(tb)))

    sys.excepthook = log_uncaught_exceptions

    raise Exception('Exception', 'test')
