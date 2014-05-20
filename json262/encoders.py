# -*- coding: utf-8 -*-

def encode_datetime(o):
    r = o.isoformat()
    if o.microsecond:
        r = r[:23] + r[26:]
    if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
    return r

def encode_date(o):
    return o.isoformat()

def encode_time(o):
    r = o.isoformat()
    if o.microsecond:
        r = r[:12]
    if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
    return r

def encode_decimal(o):
    return str(o)
