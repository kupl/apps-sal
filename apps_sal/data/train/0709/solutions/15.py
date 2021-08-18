import math
T = int(input())

for _ in range(T):
    N = int(input())
    ar = input().split()
    m = int(ar[0])

    if int(ar[N - 1]) > m:
        m = int(ar[N - 1])
    '''x = m
    for i in range(1,N):
        x = math.gcd(x,int(ar[i])) 
        if m<x :
            m = x'''

    print(m)
