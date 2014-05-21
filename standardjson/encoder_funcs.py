# -*- coding: utf-8 -*-

def encode_datetime(o):
    """ Encodes a Python datetime.datetime object as an ECMA-262 compliant
    datetime string."""
    r = o.isoformat()
    if o.microsecond:
        r = r[:23] + r[26:]
    if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
    return r

def encode_date(o):
    """ Encodes a Python datetime.date object as an ECMA-262 compliant
    date string."""
    return o.isoformat()

def encode_time(o):
    """ Encodes a Python datetime.time object as an ECMA-262 compliant
    time string."""
    r = o.isoformat()
    if o.microsecond:
        r = r[:12]
    if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
    return r

def encode_decimal(o):
    """ Encodes a Python decimal.Decimal object as an ECMA-262 compliant
    decimal string."""
    return str(o)
