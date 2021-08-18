
from collections import deque
import itertools as it
import sys
import math


def func():
    N = int(input())

    A = list(map(int, input().split()))
    P = [[(A[0], 0), (0, 0)] for i in range(2 ** (N + 1))]
    A = [0] * (2 ** N) + A

    for i in range(2 ** N + 1, 2 ** (N + 1)):
        if (A[i], i - 2**N) > P[i][0]:
            P[i][1] = P[i][0]
            P[i][0] = (A[i], i - 2**N)
        elif (A[i], i) > P[i][1]:
            P[i][1] = (A[i], i - 2**N)
        for j in range(N):
            piyo = i - 2 ** N
            if (piyo & (1 << j)) == 0:
                index = piyo + (1 << j) + 2 ** N
                for k in range(2):
                    if P[i][k] > P[index][0]:
                        P[index][1] = P[index][0]
                        P[index][0] = P[i][k]
                    elif P[i][k] > P[index][1] and P[i][k] != P[index][0]:
                        P[index][1] = P[i][k]
    ans = 0
    for i in range(2 ** N + 1, 2 ** (N + 1)):
        ans = max(ans, P[i][0][0] + P[i][1][0])
        print(ans)


func()
