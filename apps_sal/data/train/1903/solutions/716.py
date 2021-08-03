class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i != j:
                    d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    heapq.heappush(dist, (d, i, j))
        g = defaultdict(set)
        checked = set()

        def connected(a, b):
            if b in g[a]:
                return True
            if a in checked:
                return False
            checked.add(a)
            for p in g[a]:
                if connected(p, b):
                    return True
            return False
        conn = 0
        d = 0
        while conn < len(points) - 1:
            p = heapq.heappop(dist)
            checked = set()
            if not connected(p[1], p[2]):
                g[p[2]].add(p[1])
                g[p[1]].add(p[2])
                d += p[0]
                conn += 1
        return d
