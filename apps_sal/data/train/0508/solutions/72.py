import heapq
N, Q = map(int, input().split())
que = []
ans = [-1 for i in range(Q)]
D = [0 for i in range(N)]
heap = []
heapq.heapify(heap)
Set = set([])
for i in range(N):
    s, t, x = map(int, input().split())
    que.append((s - x, 0, i))
    que.append((t - x, 1, i))
    D[i] = x

for i in range(Q):
    d = int(input())
    que.append((d, 2, i))

que.sort(key=lambda x: x[0])

for x in que:
    demand = x[1]
    if demand == 0:
        heapq.heappush(heap, (D[x[2]], x[2]))
        Set.add(x[2])
    elif demand == 1:
        Set.remove(x[2])
    else:
        flag = True
        while heap and flag:
            distance, index = heapq.heappop(heap)
            if index in Set:
                ans[x[2]] = distance
                heapq.heappush(heap, (distance, index))
                flag = False
for i in range(Q):
    print(ans[i])
