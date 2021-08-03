from heapq import heappush, heappop, heapify
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
q = [(-a[i], i) for i in range(k)]
heapify(q)
res, s = [0] * n, 0
for i in range(k, n):
    heappush(q, (-a[i], i))
    x, j = heappop(q)
    s -= x * (i - j)
    res[j] = i + 1
for i in range(n, n + k):
    x, j = heappop(q)
    s -= x * (i - j)
    res[j] = i + 1
print(s)
print(*res)
