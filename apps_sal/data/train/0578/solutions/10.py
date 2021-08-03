from math import *
for j in range(int(input())):
    n, b = list(map(int, input().split()))
    a = n / (2 * b)
    a1 = ceil(a)
    a2 = floor(a)
    d = (n - a1 * b) * a1
    e = (n - a2 * b) * a2
    print(max(d, e))
