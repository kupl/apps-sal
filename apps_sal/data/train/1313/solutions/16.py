from math import *
for j in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    a = x[0]
    am = 0
    for i in range(1, n):
        a = gcd(a, x[i])
    if a == 1:
        print(-1)
    else:
        for i in range(2, int(sqrt(a)) + 1):
            if a % i == 0:
                print(i)
                am = 1
                break
        if am == 0:
            print(a)
