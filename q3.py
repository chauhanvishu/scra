# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:28:28 2018

@author: aksha
"""

def table(n,i):
  print (n*i)
  i=i+1
  if i<=10:
    table(n,i)
table(14,1)