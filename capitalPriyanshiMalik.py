# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 22:36:15 2017

@author: stusdent
"""

s = "PyThOn RoCkS"


def print_capital(s):
    
    c=0
    for i in range(len(s)):
      if s[i] >= 'A' and s[i] <= 'Z':
          c=c+1
      
        
    print(c)        

print_capital(s)    