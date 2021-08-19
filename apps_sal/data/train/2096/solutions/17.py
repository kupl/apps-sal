from collections import Counter, defaultdict, deque
import math
n = int(input())
arr = [int(x) for x in input().split()]
d = {}
visited = {}
for i in range(n):
    d[arr[i]] = i
    visited[arr[i]] = False
res = []
sarr = sorted(arr)
for el in sarr:
    cur = []
    nxt = el
    while True:
        if visited[nxt]:
            break
        visited[nxt] = True
        cur.append(d[nxt])
        nxt = sarr[d[nxt]]
    if len(cur):
        res.append(cur)
print(len(res))
for el in res:
    print(len(el), end=' ')
    for p in el:
        print(p + 1, end=' ')
    print()
