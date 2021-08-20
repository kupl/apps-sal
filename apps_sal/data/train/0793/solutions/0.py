import math
try:
    (n, d) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    z = abs(a[0] - d)
    for j in range(n):
        x = abs(a[j] - d)
        z = math.gcd(x, z)
    print(z)
except:
    pass
