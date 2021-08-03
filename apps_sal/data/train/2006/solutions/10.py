#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fractions

n = int(input())
a = list(map(int, input().split()))
m = max(a)
g = 0
for i in a:
    g = fractions.gcd(g, i)

if (m // g - n) % 2 == 0:
    print('Bob')
else:
    print('Alice')
