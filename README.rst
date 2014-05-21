===============================
standardjson
===============================

.. image:: https://badge.fury.io/py/standardjson.png
    :target: http://badge.fury.io/py/standardjson
    
.. image:: https://travis-ci.org/audreyr/standardjson.png?branch=master
        :target: https://travis-ci.org/audreyr/standardjson

.. image:: https://pypip.in/d/standardjson/badge.png
        :target: https://pypi.python.org/pypi/standardjson


JSON encoder fully compliant with the ECMA-262 and ECMA-404 specifications.

* Free software: BSD license
* Documentation: http://standardjson.readthedocs.org.

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

Use `StandardJSONEncoder` as you would use `json.JSONEncoder` from the Python standard library::

    >>> import datetime
    >>> import json
    >>> from standardjson import StandardJSONEncoder

    >>> json.dumps({'day': datetime.date(2010, 2, 17)}, cls=StandardJSONEncoder)
    '{"day": "2010-02-17"}'
