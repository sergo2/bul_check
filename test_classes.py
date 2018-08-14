# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:03:06 2018

@author: YudakovSA
"""

class BulTest(object):
    is_active = True
    def __init__(self, file_type, index_code, field):
        self.file_type = file_type
        self.index_code = index_code
        self.field = field
        
    def check(self):
        