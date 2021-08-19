# dt = {} for i in x: dt[i] = dt.get(i,0)+1
from math import sqrt
import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

for _ in range(inp()):
    n = inp()
    t = int(sqrt(n // 2) // 1)
    print(2 * t)
