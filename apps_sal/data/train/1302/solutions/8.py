#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

from math import sqrt
for _ in range(inp()):
    n = inp()
    t = int(sqrt(n//2)//1)
    print(2*t)

