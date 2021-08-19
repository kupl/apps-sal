# cook your dish here

from collections import defaultdict
d = defaultdict(int)
for i in range(97, 123):
    d[chr(i)] = 100 * (i - 96)

t = int(input())
for _ in range(t):
    s = input()
    val = defaultdict(int)
    ini = d[s[0].lower()]
    for i in range(97, 123):
        val[chr(i)] = ini + (i - 97)
    mod = (10**9) + 7
    ans = 0
    for i in s:
        ans += val[i.lower()]
        ans = ans % mod
    print(ans)
