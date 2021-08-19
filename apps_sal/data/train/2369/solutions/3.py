import sys
from collections import Counter
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    c01 = []
    c1 = [0] * (n + 1)
    for (x, y) in (list(map(int, input().split())) for _ in range(n)):
        c01.append(x)
        if y == 1:
            c1[x] += 1
    f1cnt = [[] for _ in range(n + 1)]
    cnt01 = Counter(c01)
    for (k, v) in list(cnt01.items()):
        f1cnt[v].append(c1[k])
    ans = 0
    ansf1 = 0
    for i in range(n, 0, -1):
        if f1cnt[i]:
            ans += i
            f1cnt[i].sort()
            ansf1 += min(i, f1cnt[i].pop())
            while f1cnt[i]:
                f1cnt[i - 1].append(f1cnt[i].pop())
    print(ans, ansf1)
