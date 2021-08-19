import sys
import math
from collections import defaultdict, deque
import heapq
q = int(sys.stdin.readline())
for _ in range(q):
    n = int(sys.stdin.readline())
    dic = defaultdict(list)
    for i in range(n):
        (a, b) = map(int, sys.stdin.readline().split())
        if dic[a] == []:
            dic[a] = [0, 0]
        dic[a][0] += 1
        dic[a][1] += 1 - b
    ans = 0
    cnt = 0
    heap = []
    heapq.heapify(heap)
    vis = defaultdict(int)
    for i in dic:
        heapq.heappush(heap, [-dic[i][0], dic[i][1]])
    maxlen = n
    while heap and maxlen > 0:
        (a, b) = heapq.heappop(heap)
        if vis[-a] == 1:
            heapq.heappush(heap, [a + 1, max(b - 1, 0)])
        else:
            vis[-a] = 1
            maxlen = -a - 1
            ans += -a
            cnt += b
    print(ans, ans - cnt)
