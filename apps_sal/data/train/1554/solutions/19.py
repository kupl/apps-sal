from math import gcd
for i in range(int(input())):
    (a, s) = list(map(int, input().split()))
    print(gcd(a, s) * 2)
