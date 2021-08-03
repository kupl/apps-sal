from heapq import *


class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        def manhattan(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n, g = len(A), collections.defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(A[i], A[j])
                g[i].append((d, j))
                g[j].append((d, i))

        cnt, ans, seen, q = 1, 0, [0] * n, g[0]
        seen[0] = 1

        heapify(q)

        while q:
            d, k = heappop(q)
            if seen[k]:
                continue
            seen[k], ans, cnt = 1, ans + d, cnt + 1
            for r in g[k]:
                heappush(q, r)
            if cnt >= n:
                break
        return ans
