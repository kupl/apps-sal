from math import gcd
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    if g == 1:
        print(n)
    else:
        print(-1)
