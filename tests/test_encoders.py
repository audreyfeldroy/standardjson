#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_encoders
----------------------------------

Tests for `json262.encoders` module.
"""

import unittest

from json262.encoders import encode_datetime, encode_date, encode_time

import datetime
import json


def test_encode_datetime():
    """ encode_datetime() should return a ECMA-262 compliant datetime string. """
    val = datetime.datetime(2006, 11, 21, 16, 30)
    assert encode_datetime(val) == '2006-11-21T16:30:00'

def test_encode_date():
    """ encode_date() should return a ECMA-262 compliant date string. """
    val = datetime.date(2006, 11, 21)
    assert encode_date(val) == '2006-11-21'

def test_encode_time():
    """ encode_time() should return a ECMA-262 compliant time string. """
    val = datetime.time(16, 30)
    assert encode_time(val) == '16:30:00'
