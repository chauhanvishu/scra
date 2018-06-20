# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:31:28 2018

@author: aksha
"""

def power(a,b):
  if b == 1:
    return a
  else:
    return a*power(a,b-1)
print power(6,2)
  