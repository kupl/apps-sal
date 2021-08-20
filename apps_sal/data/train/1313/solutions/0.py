from math import sqrt, gcd
for _ in range(int(input())):
    n = int(input())
    ar = [int(x) for x in input().split()]
    g = ar[0]
    for i in range(1, n):
        g = gcd(g, ar[i])
    f = g
    for i in range(2, int(sqrt(g)) + 1):
        if g % i == 0:
            f = i
            break
    if g != 1:
        print(f)
    else:
        print(-1)
