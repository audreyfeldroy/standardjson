# -*- coding: utf-8 -*-

# Avoid shadowing the standard library json module
from __future__ import absolute_import
from __future__ import unicode_literals

__author__ = 'Audrey Roy'
__email__ = 'audreyr@gmail.com'
__version__ = '0.2.0'

"""
Serialize data to/from JSON
Inspired by http://git.io/7j9pPg
"""


import datetime
import decimal
import json

from .encoder_funcs import encode_datetime, encode_date, encode_time, encode_decimal


class JSON262Encoder(json.JSONEncoder):
    """
    JSON encoder aiming to be fully compliant with ECMA-262.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            return encode_datetime(o)
        elif isinstance(o, datetime.date):
            return encode_date(o)
        elif isinstance(o, datetime.time):
            return encode_time(o)
        elif isinstance(o, decimal.Decimal):
            return encode_decimal(o)
        else:
            return super(JSON262Encoder, self).default(o)
