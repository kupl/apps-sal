# https://codeforces.com/problemset/problem/853/A
from heapq import heappush, heappop
n, k = list(map(int, input().rstrip().split()))
c = list(map(int, input().rstrip().split()))
li = [0] * n
cost = 0
q = []
for i in range(k):
    heappush(q, (-c[i], i))
for i in range(k, n):
    heappush(q, (-c[i], i))
    v, j = heappop(q)
    li[j] = i + 1
    cost += -v * (i - j)
for i in range(k):
    v, j = heappop(q)
    li[j] = n + i + 1
    cost += -v * (n + i - j)
print(cost)
print(*li)
