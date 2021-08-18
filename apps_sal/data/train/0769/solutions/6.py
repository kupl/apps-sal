from math import gcd
mod = 10**9 + 7
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    print(gcd(a, b))
