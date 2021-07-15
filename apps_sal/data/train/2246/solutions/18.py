from heapq import *

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
a = int(input())
c = list(map(int, input().split()))
cur = []
res = 0
for i, p in enumerate(arr):
    heappush(cur, c[i])
    if p <= k:
        continue
    if len(cur) * a + k < p:
        print(-1)
        return
    while p > k:
        res += heappop(cur)
        k += a
print(res)


