class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges[i].append([dist, j])
                edges[j].append([dist, i])

        cost = 0
        tree = {0}

        pq = []
        for c, v in edges[0]:
            pq.append([c, v])
        heapify(pq)

        while len(tree) < n:
            c, v = heappop(pq)
            if v in tree:
                continue
            tree.add(v)
            cost += c
            for d, u in edges[v]:
                if not u in tree:
                    heappush(pq, [d, u])
        return cost
