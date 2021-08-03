import heapq
n, k = map(int, input().split(' '))
x = list(map(int, input().split(' ')))
a = int(input())
c = list(map(int, input().split(' ')))
pq, ans = [], 0
for i in range(n):
    heapq.heappush(pq, c[i])
    while x[i] > k and len(pq) > 0:
        k += a
        ans += heapq.heappop(pq)
    if k < x[i]:
        print("-1")
        return
print(ans)
