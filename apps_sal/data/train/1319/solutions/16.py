import heapq
(n, m) = map(int, input().split())
a = []
for i in range(n + m):
    x = int(input())
    if x == -1:
        ans = heapq.heappop(a)
        print(-ans)
    else:
        heapq.heappush(a, -x)
