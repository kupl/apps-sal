from heapq import heappush, heappop, heapify
n, k = list(map(int, input().split()))
*l, = list(map(int, input().split()))
q = [(-l[i], i)for i in range(k)]
heapify(q)
a = [0] * n
s = 0
for i in range(k, n):
    heappush(q, (-l[i], i))
    x, j = heappop(q)
    s -= x * (i - j)
    a[j] = i + 1
for i in range(n, n + k):
    x, j = heappop(q)
    s -= x * (i - j)
    a[j] = i + 1
print(s)
print(' '.join(map(str, a)))
