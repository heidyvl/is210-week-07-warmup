#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""

data = [1, 2, 3.5]
def process_data(data):
    """returns addition and average"""
    
    for item in data:
        tup = (sum(data), sum(data)/len(data))
    return tup
print process_data(data)
