import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log2, ceil
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from bisect import insort
from collections import Counter
from collections import deque
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations
mod = int(1000000000.0) + 7


def ip():
    return int(stdin.readline())


def inp():
    return list(map(int, stdin.readline().split()))


def ips():
    return stdin.readline().rstrip()


def out(x):
    return stdout.write(str(x) + '\n')


t = ip()
for _ in range(t):
    n = ip()
    ans = [1] * n
    print(*ans)
