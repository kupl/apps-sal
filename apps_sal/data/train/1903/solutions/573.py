class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def cost(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        edges = [[] for _ in points]

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = cost(points[i], points[j])
                edges[i].append([dist, j])
                edges[j].append([dist, i])

        cost = 0
        tree = {0}
        pq = []
        for c, v in edges[0]:
            pq.append([c, v])

        heapify(pq)

        while len(tree) < len(points):

            c, v = heappop(pq)
            if v in tree:
                continue
            tree.add(v)
            cost += c

            for d, u in edges[v]:
                if not u in tree:
                    heappush(pq, [d, u])

        return cost
