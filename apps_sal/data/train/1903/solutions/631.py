class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        seen = set()
        cost = 0
        cnt = 0
        pq = [(0, 0)]
        while pq:
            (c, i) = heapq.heappop(pq)
            if i in seen:
                continue
            cost += c
            cnt += 1
            if cnt == N:
                return cost
            seen.add(i)
            (pt_x, pt_y) = points[i]
            for j in range(N):
                if j in seen:
                    continue
                (nei_x, nei_y) = points[j]
                nei_c = abs(pt_x - nei_x) + abs(pt_y - nei_y)
                heapq.heappush(pq, (nei_c, j))
        return cost
