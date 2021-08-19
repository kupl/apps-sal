# cook your dish here
from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    d = ar[0]
    for i in range(1, n):
        d = gcd(d, ar[i])
    if d > 1:
        print(-1)
    else:
        print(n)
