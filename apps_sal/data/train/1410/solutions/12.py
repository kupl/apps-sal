import math
f = [1]
for i in range(1, 1002):
    f.append(i * f[i - 1])


def c(n, r):
    if n < r:
        return 0
    else:
        return float(f[n] / (f[n - r] * f[r]))


t = int(input())
while t > 0:
    [s, n, m, k] = [int(i) for i in input().split()]
    ways = 0.0
    if k == 0 or s == n:
        print(float(1))
    elif k >= n:
        print(float(0))
    else:
        j = k - 1
        flag = 0
        while s - m >= 0 and j >= 0 and (n - j - 1 >= 0):
            ways = ways + c(m - 1, j) * c(s - m, n - j - 1)
            j -= 1
        p = ways / c(s - 1, n - 1)
        p = 1 - p
        print(p)
    t -= 1
