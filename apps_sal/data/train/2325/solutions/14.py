# ARC071E

import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))


s = input()
t = input()

sa = [0] * (len(s) + 1)
sb = [0] * (len(s) + 1)
ta = [0] * (len(t) + 1)
tb = [0] * (len(t) + 1)

ca = 0
cb = 0
for i, c in enumerate(s):
    if c == "A":
        ca += 1
    else:
        cb += 1
    sa[i + 1] = ca
    sb[i + 1] = cb
ca = 0
cb = 0
for i, c in enumerate(t):
    if c == "A":
        ca += 1
    else:
        cb += 1
    ta[i + 1] = ca
    tb[i + 1] = cb


q = int(input())
for i in range(q):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())
    if (((sa[b + 1] - sa[a]) - (sb[b + 1] - sb[a])) - ((ta[d + 1] - ta[c]) - (tb[d + 1] - tb[c]))) % 3 == 0:
        print("YES")
    else:
        print("NO")
