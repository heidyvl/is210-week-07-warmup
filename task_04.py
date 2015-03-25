#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


def process_data(data):
    """returns addition and average"""
    avg = 0.0
    for item in data:
        avg += item
        tup = (sum(data), avg/len(data))
    return tup
