#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

def func():
    N = int(input())

    A = list(map(int, input().split()))
    P = [[(A[0], 0), (0, 0)] for i in range(2 ** N)]

    for i in range(1, 2 ** N):
        if (A[i], i) > P[i][0]:
            P[i][1] = P[i][0]
            P[i][0] = (A[i], i)
        elif (A[i], i) > P[i][1]:
            P[i][1] = (A[i], i)
        for j in range(N):
            if (i & (1 << j)) == 0:
                index = i + (1 << j)
                for k in range(2):
                    if P[i][k] > P[index][0]:
                        P[index][1] = P[index][0]
                        P[index][0] = P[i][k]
                    elif P[i][k] > P[index][1] and P[i][k] != P[index][0]:
                        P[index][1] = P[i][k]
    ans = 0
    for i in range(1, 2 ** N):
        ans = max(ans, P[i][0][0] + P[i][1][0])
        print(ans)
    #print(P)

func()
