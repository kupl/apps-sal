# cook your dish here
import math
T = int(input())
for i in range(T):
    a = list(map(int, input().split()))
    n = a[0]
    m = a[1]
    print(m * n // math.gcd(m, n))
