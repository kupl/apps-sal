from math import *
t = int(input())
for _ in range(t):
    (x, y) = map(int, input().split())
    k = gcd(x, y)
    if k == 1:
        print('YES')
    else:
        print('NO')
