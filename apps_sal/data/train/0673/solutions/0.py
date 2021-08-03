from math import gcd
from math import ceil
from itertools import combinations as c
t = int(input())
for _ in range(t):
    n, m, a, d = list(map(int, input().split()))

    l = []
    for i in range(5):
        l.append(a + i * d)
    ans = m - n + 1
    for i in range(1, 6):
        x = list(c(l, i))
        for j in x:
            e = j[0]
            for v in j:
                e = (e * v) // gcd(e, v)
            # print(e)
            if i % 2:
                ans -= m // e - (n - 1) // e
            else:
                ans += m // e - (n - 1) // e
    print(ans)
