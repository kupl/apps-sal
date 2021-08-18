
import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/19 21:52

"""

S = input()

N = len(S)
ans = 0
for i in range(N):
    if S[i] != 'Q':
        continue
    for j in range(i + 1, N):
        if S[j] != 'A':
            continue
        for k in range(j + 1, N):
            if S[k] == 'Q':
                ans += 1

print(ans)
