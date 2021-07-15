# cook your dish here
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:24:15 2020

@author: Admin
"""

for _ in range(int(input())):
 n=int(input())
 l=[int(i) for i in input().split()]
 g=sorted(l,reverse=True)
 s=0
 for r in range(0,len(l),2):
  s+=g[r]
 print(s)
