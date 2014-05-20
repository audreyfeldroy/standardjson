#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_encoders
----------------------------------

Tests for `json262.encoders` module.
"""

import unittest

from json262.encoders import encode_datetime

import datetime
import json


def test_encode_datetime():
    """ JSON262Encoder should work with datetimes. """
    val = datetime.datetime(2006, 11, 21, 16, 30)
    assert encode_datetime(val) == '2006-11-21T16:30:00'
