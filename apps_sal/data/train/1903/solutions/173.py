import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        pq = []
        p1 = points[0]
        seen_idxs = {0}
        for idx in range(len(points)):
            if idx not in seen_idxs:
                p2 = points[idx]
                heapq.heappush(pq, (manhattan(p1, p2), idx))
            else:
                continue
        total_dist = 0
        while len(seen_idxs) != len(points):
            while pq[0][-1] in seen_idxs:
                heapq.heappop(pq)
            (dist, min_idx) = heapq.heappop(pq)
            total_dist += dist
            seen_idxs.add(min_idx)
            p1 = points[min_idx]
            for idx in range(len(points)):
                if idx not in seen_idxs:
                    p2 = points[idx]
                    heapq.heappush(pq, (manhattan(p1, p2), idx))
        return total_dist
