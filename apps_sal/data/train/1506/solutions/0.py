import sys
import os
import io
import time
import copy
import math
import queue
import bisect
from collections import deque
from functools import lru_cache
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
sys.setrecursionlimit(100000000)


def main():
    (n, m) = map(int, input().split())
    mat = []
    for _ in range(n):
        s = input()
        a = []
        for i in s:
            a.append(int(i))
        mat.append(a)
    Q = int(input())
    ans = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(Q):
        (x1, y1, x2, y2) = map(int, input().split())
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        ans[x1][y1] += 1
        ans[x2 + 1][y1] -= 1
        ans[x1][y2 + 1] -= 1
        ans[x2 + 1][y2 + 1] += 1
    for j in range(m + 1):
        for i in range(1, n + 1):
            ans[i][j] = ans[i - 1][j] + ans[i][j]
    for i in range(n + 1):
        for j in range(1, m + 1):
            ans[i][j] = ans[i][j - 1] + ans[i][j]
    for i in range(n):
        for j in range(m):
            mat[i][j] = (ans[i][j] + mat[i][j]) % 2
    for m in mat:
        for i in m:
            print(i, end='')
        print('')


main()
