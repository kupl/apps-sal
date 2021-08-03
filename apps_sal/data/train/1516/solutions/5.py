# cook your dish here
import math
t = int(input())
for _ in range(t):
    m = 10**9 + 7
    p = 0
    s = 0
    n, k = list(map(int, input().split()))
    if(n == 2):
        print(((k * (k - 1)) // 2) % m)
    else:
        while((k - 1 - p * (n - 1)) > 0):
            s += k - 1 - p * (n - 1)
            p += 1
        print(s)
