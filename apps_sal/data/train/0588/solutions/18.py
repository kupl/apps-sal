from math import gcd
T = int(input())
x = []
for i in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    g = a[1] - a[0]
    for i in range(1, n):
        g = gcd(g, a[i] - a[i - 1])
    g = gcd(g, 360 - a[n - 1] + a[0])
    count = 0
    for i in range(1, n):
        count += (a[i] - a[i - 1]) // g - 1
    count += (360 - a[n - 1] + a[0]) // g - 1
    print(count)
