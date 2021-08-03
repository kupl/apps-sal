from math import *
t = int(input())
for i in range(0, t):
    a, b = input().split()
    a, b = int(a), int(b)
    c = ""
    for j in range(1, a + 1):
        c += str(j)
    for j in range(1, a):
        c += str(a - j)
    c = int(c)
    b *= b
    c = c * b
    c = str(c)
    mod = 10**9 + 7
    ans = 0
    for j in range(0, len(c)):
        ans += (((23**j) % mod) * (int(c[j]) % mod)) % mod
    ans = ans % mod
    print(ans)
