# cook your dish here
import math
t = int(input())
for _ in range(t):
    m = 10**9 + 7
    s = 0
    n, k = list(map(int, input().split()))
    if(n == 2):
        print(((k * (k - 1)) // 2) % m)
    else:
        p = (k - 1) // (n - 1)
        s = (((p + 1) * (2 * k - n * p + p - 2)) // 2) % m
        print(s)
