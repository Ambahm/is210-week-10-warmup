#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Misc. dictionary"""

import data

CORRECTED = data.BANDS.copy()                       # Copying values

CORRECTED['Dylan'] = ['vocals', 'guitar', 'harmonica']

del data.BANDS['Van Halen']['David Lee Roth']       # Deleting

CORRECTED['Van Halen']['Sammy Hagar'] = ['vocals']  # Adding




if __name__ == '__main__':
    print 'ORIGINAL BANDS: \n', data.BANDS.keys()
    #print 'Van Halen KEYS     ', CORRECTED['Van Halen'].keys()
    print '\nADDED BANDS\n:', CORRECTED.keys()
    print '\nADDED VALUES: \n', CORRECTED['Dylan']
    print '\nVan Helen REVISED: \n', CORRECTED['Van Halen']
