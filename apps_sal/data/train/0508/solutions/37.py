import heapq
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
L1 = []
for i in range(n):
    L1.append((l[i][0] - l[i][2], 1, l[i][2]))
    L1.append((l[i][1] - l[i][2], -1, l[i][2]))
for i in range(q):
    L1.append((int(input()), 2, 0))
L1.sort()
L2 = []
heapq.heapify(L2)
L3 = []
L3 = set(L3)
for i in range(len(L1)):
    if L1[i][1] == 1:
        heapq.heappush(L2, L1[i][2])
        L3.add(L1[i][2])
    elif L1[i][1] == -1:
        L3.remove(L1[i][2])
    else:
        while L2 and L2[0] not in L3:
            heapq.heappop(L2)
        if L2:
            print(L2[0])
        else:
            print(-1)
