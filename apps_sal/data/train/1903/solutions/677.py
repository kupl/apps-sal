class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dis[i].append((d, j))
                dis[j].append((d, i))
        (ans, seen, heap) = (0, set(), [(0, 0)])
        while len(seen) < len(points):
            (d, j) = heapq.heappop(heap)
            if j not in seen:
                seen.add(j)
                ans += d
                for (d, i) in dis[j]:
                    heapq.heappush(heap, (d, i))
        return ans
