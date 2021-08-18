from math import gcd as g
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    gc = g(a, b)
    r = (a // gc) * (b // gc)
    print(r)
