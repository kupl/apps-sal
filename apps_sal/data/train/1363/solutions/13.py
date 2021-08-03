from math import *
t = int(input())
for i in range(0, t):
    a, b = input().split()
    a, b = int(a), str(b)
    c = ""
    for j in range(0, a):
        c += b
    c = int(c)
    c = c**2
    c = str(c)
    mod = 10**9 + 7
    ans = 0
    for j in range(0, len(c)):
        ans += (((23**j) % mod) * (int(c[j]) % mod)) % mod
    ans = ans % mod
    print(ans)
