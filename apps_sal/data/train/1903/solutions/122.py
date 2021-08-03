import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattanDistance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)

        distsMap = {}
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distsMap[(i, j)] = manhattanDistance(x1, y1, x2, y2)
                distsMap[(j, i)] = distsMap[(i, j)]

        result = 0
        pq = [(0, 0)]
        seen = set()
        minDists = {i: float('inf') for i in range(n)}
        while len(pq) != 0:
            (dist, i) = heapq.heappop(pq)
            # print(dist,i)
            if i in seen:
                continue
            seen.add(i)
            result += dist

            minDists[i] = 0
            for j in range(n):
                if j in seen:
                    continue
                minDists[j] = min(minDists[j], distsMap[(i, j)])
                heapq.heappush(pq, (minDists[j], j))

            # for j in range(n):
            #     if j in seen:
            #         continue
            #     # nextDist = min(distsMap[(ip,j)] for ip in seen)
            #     heapq.heappush(pq, (minDists[j],j) )
                # for ip in seen:

        return result
