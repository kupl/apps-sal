#!/usr/bin/env python3
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().rstrip() + "#"
    max_l = 0
    seq_l = 0
    for ch in s:
        if ch == "L":
            seq_l += 1
        else:
            max_l = max(max_l, seq_l)
            seq_l = 0
    print(max_l + 1)
