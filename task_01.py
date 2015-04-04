#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Multiarray dictionary"""

# key:value
# key[key:[key:value]


GRADE_DATA = {
    'Luke Skywalker':{
        'subject':{
            'math':'B', 'etiquette':'B+', 'grammar':'B', 'gym':'A'
        }
    },
    'Han Solo':{
        'subject':{
            'math':'A-', 'etiquette':'C-', 'grammar':'B', 'gym':'B'
        }
    },
    'C-3PO':{
        'subject':{
            'math':'C', 'etiquette':'A+', 'grammar':'A', 'gym':'F'
        }
    }
}


if __name__ == '__main__':
    print GRADE_DATA.keys()
    print 'HAN SOLO \n', GRADE_DATA['Han Solo']
    print GRADE_DATA['Han Solo']['subject']
    print GRADE_DATA['Han Solo']['subject']['grammar']
