#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())

l = [0] * 7
for _ in range(n):
    s = input()
    for i in range(7):
        l[i] += int(s[i])

print(max(l))
