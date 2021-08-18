import sys
from math import gcd
def input(): return sys.stdin.readline().strip()


def inp(): return list(map(int, sys.stdin.readline().strip().split()))


for _ in range(int(input())):
    n, k = map(int, input().split())
    d = [[] for i in range(k + 1)]
    for i in range(n):
        l, r, p = map(int, input().split())
        d[p].append([l, r])
    ans = 0
    for i in d:
        if len(i) == 0:
            continue
        ans += 1
        t = sorted(i, key=lambda x: (x[1], x[0]))
        final = t[0][1]
        for j in range(1, len(t)):
            if t[j][0] >= final:
                ans += 1
                final = t[j][1]
    print(ans)
