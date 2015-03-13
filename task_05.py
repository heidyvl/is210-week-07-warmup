#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""

to_flip = [(1, 2, 3), 'hello']
i = 0
def flip_keys(to_flip):
    for i in to_flip:
        to_flip[:i]
        i += 1
    return to_flip
print flip_keys(to_flip)
        


    
        
