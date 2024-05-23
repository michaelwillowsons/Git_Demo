# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:46:29 2024

@author: willom
"""
# function to add two numbers
# Default values: 1,2,0
def add(a=1,b=2, c=0):
    ans = a+b +c
    return ans

print(add(3,4))

# test case
# 5+6=11

if add(5,6) ==11:
    print("Test passed")