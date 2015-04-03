#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assign /Access values from dictionary"""

import data


# key:value
# Accessing Nigel Tufnel from Spinal Tap Band
NIGEL = data.BANDS['Spinal Tap']['Nigel Tufnel']

# Getting names of Band i.e key values from variable BAND
BANDS_NAMES = data.BANDS.keys()


if __name__ == '__main__':
    print 'NIGEL INSTRUMENTS:\n', NIGEL, '\nKEY BANDS:\n: ', BANDS_NAMES
