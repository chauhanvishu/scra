# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:31:46 2018

@author: aksha
"""

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))