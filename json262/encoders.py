# -*- coding: utf-8 -*-

def encode_datetime(o):
    r = o.isoformat()
    if o.microsecond:
        r = r[:23] + r[26:]
    if r.endswith('+00:00'):
        r = r[:-6] + 'Z'
    return r
