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

FAQ
----

Does StandardJSONEncoder provide info about the Python type of the object?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. `StandardJSONEncoder` purposely does not, in favor of a human-style,
type-agnostic approach. 

When encoded by `StandardJSONEncoder`, there is no differentiation between
the string `"2010-02-17"` and the date object `date(2010, 2, 17)}`. This is
the same approach described in ECMA-404, Introduction, paragraph 2:

"JSON is agnostic about numbers. In any programming language, there can be a variety of number types of various capacities and complements, fixed or floating, binary or decimal. That can make interchange between different programming languages difficult. JSON instead offers only the representation of numbers that humans use: a sequence of digits. All programming languages know how to make sense of digit sequences even if they disagree on internal representations. That is enough to allow interchange."

What if my application requires Python language-dependent JSON?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In that case, it's not a good use case for this package. The use case I have in mind is for taking Python objects and turning them into language-independent JSON. This is in the spirit of what JSON is designed for.

As described on json.org:

"JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language."

Most real-world use cases of JSON should be fine with language-independent JSON, of course.