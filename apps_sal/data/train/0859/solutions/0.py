import math
import os
import random
import re
import sys


r = 100000
prev = 1
s = set()
for i in range(1, r+1):
    now = i ^ prev
    s.add(now)
    prev = now
s = list(s)
t = int(input())
while t > 0:
    t -= 1
    n, k = list(map(int, input().split()))

    if n > 3:
        if n % 2 == 0:
            size = (n//2) + 2
        else:
            size = ((n-1)//2) + 2
    else:
        size = n
    if size - k >= 0:
        print(s[size-k])
    else:
        print(-1)

