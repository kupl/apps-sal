# cook your dish here
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:53:59 2020

@author: srira
"""
count = 0
for N in range(int(input())):
    b, d = map(int, input().split())
    if b >= 0:
        count += d - b + 1
    else:
        count += d + abs(b) + 1
print(count % (10**9 + 7))
