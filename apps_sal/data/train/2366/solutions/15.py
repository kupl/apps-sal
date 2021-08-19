from sys import stdin, stdout
from collections import defaultdict
from collections import deque
import math
import copy
T = int(input())
for i in range(T):
    N = int(input())
    arr = [int(x) for x in stdin.readline().split()]
    mini = [0] * N
    m = arr[-1]
    for i in range(N - 1, -1, -1):
        m = min(m, arr[i])
        mini[i] = m
    res = 0
    for i in range(N - 1):
        if arr[i] > mini[i + 1]:
            res += 1
    print(res)
