from math import *
t = int(input())
for i in range(t):
    (m, b) = input().split()
    m = int(m)
    b = int(b)
    print(2 * gcd(m, b))
