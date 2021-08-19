from math import gcd
for i in range(int(input())):
    (a, b) = map(int, input().split())
    c = a * b
    d = gcd(a, b)
    print(c // d)
