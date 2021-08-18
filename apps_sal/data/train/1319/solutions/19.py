import heapq
a, b = list(map(int, input().split()))
numList = []
for i in range(a + b):
    numIn = int(input())
    if numIn == -1:
        ans = heapq.heappop(numList)
        print(-ans)
    else:
        heapq.heappush(numList, -numIn)
