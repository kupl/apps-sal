import math
t = int(input())
while t != 0:
    t -= 1
    (n, a, k) = list(map(int, input().split()))
    g = n * (n - 1)
    d = 360 * (n - 2) - 2 * a * n
    f = a * g + (k - 1) * d
    j = math.gcd(f, g)
    b = f // j
    e = g // j
    print(b, e)
