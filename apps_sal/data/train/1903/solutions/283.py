class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        q = []
        for i in range(1, len(points)):
            heapq.heappush(q, (manhattan(points[0], points[i]), 0, i))
        network = set([0])
        res = 0
        while q and len(network) < len(points):
            (d, prev, node) = heapq.heappop(q)
            if node in network:
                continue
            network.add(node)
            res += d
            for neigh in range(len(points)):
                if neigh not in network:
                    heapq.heappush(q, (manhattan(points[neigh], points[node]), node, neigh))
        return res
