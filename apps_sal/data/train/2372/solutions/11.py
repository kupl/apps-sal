# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:20:28 2020

@author: Dark Soul
"""
import math
t = int(input(''))
for _ in range(t):
    n = int(input(''))
    x = math.sqrt(n)
    if x == int(x):
        x = int(x)
        sol = (n // x) - 1
        sol += (x - 1)
        print(sol)
    else:
        x = int(x) + 1
        sol = n // x
        if sol * x == n:
            sol -= 1
        sol += (x - 1)
        print(sol)
