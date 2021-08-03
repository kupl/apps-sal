import sys
from bisect import bisect


def input():
    return sys.stdin.readline()[:-1]


x = int(input())
k = int(input())
z = [0] + list(map(int, input().split()))
s = [z[i + 1] - z[i] for i in range(k)]

lr = [[0, x]]
pq = [[0, x]]

for i in range(k):
    l, r = lr[-1]
    p, q = pq[-1]
    if i % 2 == 0:
        lr.append([max(l - s[i], 0), max(r - s[i], 0)])
        pq.append([min(p + max(min(s[i], x) - l, 0), q), q])
    else:
        lr.append([min(l + s[i], x), min(r + s[i], x)])
        pq.append([p, max(q - max(r - max(x - s[i], 0), 0), p)])

q = int(input())
for _ in range(q):
    t, a = map(int, input().split())
    i = bisect(z, t) - 1
    t -= z[i]
    if a <= pq[i][0]:
        y = lr[i][0]
    elif a >= pq[i][1]:
        y = lr[i][1]
    else:
        y = lr[i][0] + a - pq[i][0]

    if i % 2 == 0:
        print(max(y - t, 0))
    else:
        print(min(y + t, x))
