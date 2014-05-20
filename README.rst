===============================
json262
===============================

.. image:: https://badge.fury.io/py/json262.png
    :target: http://badge.fury.io/py/json262
    
.. image:: https://travis-ci.org/audreyr/json262.png?branch=master
        :target: https://travis-ci.org/audreyr/json262

.. image:: https://pypip.in/d/json262/badge.png
        :target: https://pypi.python.org/pypi/json262


JSON encoder fully compliant with ECMA-262 specification.

* Free software: BSD license
* Documentation: http://json262.readthedocs.org.

Features
--------

Support for all objects that the Python stdlib's `json.JSONEncoder` can encode, plus:

* `datetime.datetime`
* `datetime.date`
* `datetime.time`
* `decimal.Decimal`

Works on Python 2.6, 2.7, 3.3. Probably works on 3.4 and 3.5 but I haven't set up tests for those with Tox yet.

Quickstart
----------

Use `JSON262Encoder` as you would use `json.JSONEncoder` from the Python standard library::

    >>> import datetime
    >>> import json
    >>> from json262 import JSON262Encoder

    >>> json.dumps({'day': datetime.date(2010, 2, 17)}, cls=JSON262Encoder)
    '{"day": "2010-02-17"}'
