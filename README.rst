dynamolog: Python centralized logging using DynamoDB
=======================================================

:Info: Python centralized logging using DynamoDB.
:Author: `Jose Luis Lopez Pino`_
:Maintainer: `Jose Luis Lopez Pino`_

Setup
-----

Before using this handler for logging you will need to create a table in Amazon DynamoDB.


Usage
-----

>>> import logging
>>> from dynamolog import DynamoHandler

>>> log = logging.getLogger('example')
>>> log.setLevel(logging.DEBUG)

>>> handler = DynamoHandler.to('table_name',
                               'dynamodb_region',
                               'dynamodb_key',
                               'dynamodb_secret')
>>> log.addHandler(handler)

>>> log.debug("1 - debug message")
>>> log.info("2 - info message")
>>> log.warn("3 - warn message")
>>> log.error("4 - error message")
>>> log.critical("5 - critical message")
>>> log.debug("debug message with arguments %s %s %s", 1, "2", 3)

Check the sample for more details.



Acknowledgements
-----

This package is heavily inspired by mongodb-log <https://github.com/puentesarrin/mongodb-log>




.. _Jose Luis Lopez Pino: https://github.com/jllopezpino
