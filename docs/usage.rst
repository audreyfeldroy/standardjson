========
Usage
========

Use `JSON262Encoder` as you would use `json.JSONEncoder` from the Python standard library::

    >>> import datetime
    >>> import json
    >>> from json262 import JSON262Encoder

    >>> json.dumps({'day': datetime.date(2010, 2, 17)}, cls=JSON262Encoder)
    '{"day": "2010-02-17"}'

You can encode a single Python data structure too::

    >>> JSON262Encoder().encode({'day': datetime.date(2010, 2, 17)})
    '{"day": "2010-02-17"}'
