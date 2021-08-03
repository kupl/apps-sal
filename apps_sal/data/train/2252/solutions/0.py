#!/usr/bin/env python3
"""
Created on Wed Feb 28 11:47:12 2018

@author: mikolajbinkowski
"""
import sys

N = int(input())

string_count = {}
for _ in range(N):
    s = str(input())
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    s0 = []
    for a in 'abcdefghijklmnopqrstuvwxyz':
        if char_count.get(a, 0) % 2 == 1:
            s0.append(a)
    s1 = ''.join(s0)
    string_count[s1] = string_count.get(s1, 0) + 1

pairs = 0
for s, v in list(string_count.items()):
    pairs += v * (v - 1) // 2
    for i in range(len(s)):
        pairs += v * string_count.get(s[:i] + s[i + 1:], 0)

print(pairs)
