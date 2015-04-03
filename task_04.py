#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Update nested to dictionary"""

import data


data.BANDS['Fleetwood Mac'].update({
    'Buckingham Nicks':{
        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Stevie Nicks': ['vocals', 'tambourine']
    }})

if __name__ == '__main__':
    print 'ORIGINAL BANDS:\n', data.BANDS.keys()
    print '\nFleetwood Mac values:\n', data.BANDS['Fleetwood Mac'].keys()
