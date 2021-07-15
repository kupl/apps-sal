# -*- coding: utf-8 -*-
from time import perf_counter
from sys import stdin

def run(n, s):
    m = 0
    small = n // 2
    for big in range(n-1, (n+1)//2-1, -1):
        while small >= 0 and s[small] > s[big] / 2:
            small -= 1
        if small == -1:
            break
        #print(small, big)
        small -= 1
        m += 1
    print(n-m)

def run2(n, s):
    r = n - 1
    l = n // 2 - 1
    result = 0
    while l >= 0:
        if s[l] * 2 <= s[r]:
            result += 1
            r -= 1
        l -= 1
    print(n - result)

n = int(input())
s = sorted([int(x) for x in stdin.read().strip().split('\n')])
run(n, s)

