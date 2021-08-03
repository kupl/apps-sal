import heapq
n = int(input())
d = list(map(int, input().split()))
pq = [-d[0]]
heapq.heapify(pq)
ans = 0
for i in range(1, n):
    temp = i - d[i]
    heapq.heappush(pq, temp)
    if heapq.nsmallest(1, pq)[0] < temp:
        ans += temp - heapq.nsmallest(1, pq)[0]
        heapq.heappushpop(pq, temp)
print(ans)
