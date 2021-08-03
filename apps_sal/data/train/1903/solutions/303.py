class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        q = []
        for i in range(1, len(points)):
            heapq.heappush(q, (manhattan(points[0], points[i]), 0, i))

        network = set([0])
        res = 0
        while q and (len(network) < len(points)):

            d, i, j = heapq.heappop(q)

            if j in network:
                continue

            network.add(j)
            res += d

            for k in range(len(points)):
                if (k != j) and (k not in network):
                    heapq.heappush(q, (manhattan(points[k], points[j]), j, k))

        return res
