import math
T = int(input())
for _ in range(T):
    N = int(input())
    ar = input().split()
    m = int(ar[0])
    if int(ar[N - 1]) > m:
        m = int(ar[N - 1])
    'x = m\n    for i in range(1,N):\n        x = math.gcd(x,int(ar[i])) \n        if m<x :\n            m = x'
    print(m)
