# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 28/06/2020

from sys import stdin,stdout
from math import gcd, ceil, sqrt
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
mod = 1000000007

tc = ii1()
for _ in range(tc):
    p, q, r = iia()
    a, b, c = iia()
    if a < p or b < q or c < r:
        print(-1)
    else:
        add = [a - p, b - q, c - r]
        print(sum(add))


