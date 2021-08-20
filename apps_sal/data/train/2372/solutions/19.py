from math import ceil
for tc in range(int(input())):
    n = int(input())
    s = ceil(n ** 0.5)
    t = n ** 0.5 // 1
    sans = ceil(n / s) + s
    tans = ceil(n / t) + t
    print(max(min(sans, tans) - 2, 0))
