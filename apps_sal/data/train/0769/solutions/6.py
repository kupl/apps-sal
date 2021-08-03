# cook your dish here
from math import gcd
mod = 10**9 + 7
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    # c = pow(a,b-2,b)
    # print(gcd(a,c))
    print(gcd(a, b))
