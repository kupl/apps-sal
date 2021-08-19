import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = [(0, 0)]
        heapq.heapify(q)
        added = [False for i in range(len(points))]
        ans = 0
        while q:
            (d, u) = heapq.heappop(q)
            if added[u]:
                continue
            ans += d
            added[u] = True
            for i in range(len(points)):
                if added[i]:
                    continue
                dist = abs(points[i][0] - points[u][0])
                dist += abs(points[i][1] - points[u][1])
                heapq.heappush(q, (dist, i))
        return ans
