#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


def flip_keys(to_flip):
    """to_flip list returns a list"""
    i = 0
    for item in to_flip:
        to_flip[i] = item[::-1]
        i += 1
    return to_flip
