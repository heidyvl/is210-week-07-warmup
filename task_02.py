#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""

import data
BALLETS = data.BALLETS
del BALLETS[11]
BALLETS[1] =  'Swan Lake'
BALLETS.append('Herman Schmerman')
EXTENDED_LIST = ['Don Quixote', 'Sylvia']
BALLETS.extend(EXTENDED_LIST)

