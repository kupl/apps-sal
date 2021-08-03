from math import gcd, sqrt
for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    g = 0
    for i in l:
        g = gcd(g, i)
    if(g < n):
        print(n - g)
        continue
    f = 0
    s = int(sqrt(g))
    for i in range(1, s + 1):
        if(g % i == 0):
            if(i <= n):
                f = max(f, i)
            if(g // i <= n):
                f = max(f, g // i)
    print(n - f)
