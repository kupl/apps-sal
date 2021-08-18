import numpy as np
import math
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    aa = np.zeros([n], dtype=int)
    for i in range(n - 1):
        aa[i] = a[i + 1] - a[i]
    aa[n - 1] = 360 - a[n - 1] + a[0]
    hcf = 180
    for i in range(n):
        hcf = min(hcf, math.gcd(aa[i % n], aa[(i + 1) % n]))
    print(360 // hcf - n)
