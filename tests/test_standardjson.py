#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_standardjson
----------------------------------

Tests for `standardjson` module.
"""

import unittest

from standardjson import StandardJSONEncoder

import datetime
import json


# Unit tests
def test_json_encoder_date():
    """ StandardJSONEncoder should work with dates. """
    encoder = StandardJSONEncoder()
    items = encoder.default(datetime.date(2010, 2, 17))
    assert items == '2010-02-17'


def test_json_encoder_datetime():
    """ StandardJSONEncoder should work with datetimes. """
    encoder = StandardJSONEncoder()
    items = encoder.default(datetime.datetime(2006, 11, 21, 16, 30))
    assert items == '2006-11-21T16:30:00'


def test_json_encoder_time():
    """ StandardJSONEncoder should work with times. """
    encoder = StandardJSONEncoder()
    items = encoder.default(datetime.time(16, 30))
    assert items == '16:30:00'


def test_json_encoder_time_microsecond():
    """ StandardJSONEncoder should work with times with microsecond info.
        ECMA-262 says, "sss is the number of complete milliseconds since the
        start of the second as three decimal digits." """
    encoder = StandardJSONEncoder()
    items = encoder.default(datetime.time(16, 30, 1, 123456))
    assert items == '16:30:01.123'


def test_json_encoder_time_tzinfo():
    """ StandardJSONEncoder should work with times with timezone info.
        ECMA-262 specifies that time zone offset can be like ZHH:mm, +HH:mm,
        or -HH:mm. """
    encoder = StandardJSONEncoder()

    class GMT1(datetime.tzinfo):
        def utcoffset(self, dt):
            return datetime.timedelta(hours=1)

        def dst(self, dt):
            return datetime.timedelta(0)

        def tzname(self, dt):
            return "Europe/Prague"
    items = encoder.default(datetime.time(16, 30, 1, tzinfo=GMT1()))
    assert items == '16:30:01+01:00'


def test_json_encoder_time_tzinfo_gmt():
    """ StandardJSONEncoder should work with times with timezone info.
        ECMA-262 specifies that time zone offset can be like ZHH:mm, +HH:mm,
        or -HH:mm. """
    encoder = StandardJSONEncoder()

    class GMT(datetime.tzinfo):
        def utcoffset(self, dt):
            return datetime.timedelta(hours=0)

        def dst(self, dt):
            return datetime.timedelta(0)

        def tzname(self, dt):
            return "GMT"
    items = encoder.default(datetime.time(16, 30, 1, tzinfo=GMT()))
    assert items == '16:30:01Z'


# Integration tests
def test_json_encoder_date_json():
    """ StandardJSONEncoder should work with dates. Pass in as dumps() cls parameter. """
    items = json.dumps({'day': datetime.date(2010, 2, 17)}, cls=StandardJSONEncoder)
    assert items == '{"day": "2010-02-17"}'


def test_json_encoder_date2_json():
    """ StandardJSONEncoder should work with dates. Test via encode()."""
    items = StandardJSONEncoder().encode({'day': datetime.date(2010, 2, 17)})
    assert items == '{"day": "2010-02-17"}'


def test_json_encoder_datetime_json():
    """ StandardJSONEncoder should work with datetimes. Pass in as dumps() cls parameter. """
    items = json.dumps({'day_and_time': datetime.datetime(2006, 11, 21, 16, 30)}, cls=StandardJSONEncoder)
    assert items == '{"day_and_time": "2006-11-21T16:30:00"}'
