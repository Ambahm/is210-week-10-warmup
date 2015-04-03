#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 10, Task 05"""


import data

data.SUPERHEROES['Logan']['alias'] = 'Wolverine'

if __name__ == '__main__':

    #print 'SUPERHEROES:\n', data.SUPERHEROES.keys()
    print data.SUPERHEROES['Logan']
    print data.SUPERHEROES['Logan']['alias']
