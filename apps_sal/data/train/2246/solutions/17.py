import heapq as hp
import sys
(n, k) = map(int, input().split())
arr = list(map(int, input().split()))
p = int(input())
arrx = list(map(int, input().split()))
prev = []
hp.heapify(prev)
cost = 0
flag = 0
for i in range(n):
    hp.heappush(prev, arrx[i])
    while arr[i] > k and len(prev) > 0:
        k += p
        cost += hp.heappop(prev)
    if k < arr[i]:
        flag = 1
        break
if flag == 1:
    print(-1)
else:
    print(cost)
