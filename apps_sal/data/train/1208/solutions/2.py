# dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys
input = sys.stdin.readline
inp, ip = lambda: int(input()), lambda: [int(w) for w in input().split()]

M = 10**9 + 7
f = [1] * (1000001)
for i in range(2, 1000001):
    f[i] = (i * f[i - 1]) % M
for i in range(2, 1000001):
    f[i] = (f[i] * f[i - 1]) % M

for _ in range(inp()):
    n = inp()
    print(f[n])
