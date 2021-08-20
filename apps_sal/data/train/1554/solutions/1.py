from math import *
n = int(input())
for i in range(n):
    (b, m) = input().split()
    b = int(b)
    m = int(m)
    print(2 * gcd(b, m))
