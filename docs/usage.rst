========
Usage
========

Use `StandardJSONEncoder` as you would use `json.JSONEncoder` from the Python standard library::

    >>> import datetime
    >>> import json
    >>> from standardjson import StandardJSONEncoder

    >>> json.dumps({'day': datetime.date(2010, 2, 17)}, cls=StandardJSONEncoder)
    '{"day": "2010-02-17"}'

You can encode a single Python data structure too::

    >>> StandardJSONEncoder().encode({'day': datetime.date(2010, 2, 17)})
    '{"day": "2010-02-17"}'
