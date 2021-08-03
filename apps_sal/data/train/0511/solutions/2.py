#!/usr/bin/env python3

# import
#import math
#import numpy as np
N = int(input())
A = list(map(int, input().split()))

t = 0
for a in A:
    t = t ^ a

ans = [str(t ^ A[i]) for i in range(N)]

print(" ".join(ans))
