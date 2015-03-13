#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""

from decimal import Decimal
data = [1, 2, 3]
def process_data(data):
    for i in range(len(data)):
       tup = [sum(data), float(sum(data)/len(data))]
    return tup
print process_data(data)
