# cook your dish here
import math
for t in range(int(input())):
    n, m = list(map(int, input().split()))
    area = n * m
    res = math.gcd(n, m)
    res = res**2
    print(area // res)
