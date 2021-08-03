# cook your dish here
from sys import stdin, stdout, setrecursionlimit
from math import ceil

mod = 1000000007
t = int(stdin.readline())
for _ in range(t):
    m, n = list(map(int, input().split()))
    if m < n:
        m, n = n, m

    y = n - 1
    s1 = ((y * (y + 1)) // 2) % mod
    s2 = ((y * (y + 1) * (2 * y + 1)) // 6) % mod
    s3 = ((y * y * (y + 1) * (y + 1)) // 4) % mod

    ans = (m * n * s1 - (m + n) * s2 + s3) % mod
    # ans = (m*(m+1)*(2*m*n + 4*n + 2 - m*m - m)//12)

    print(ans)
