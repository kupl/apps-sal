class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodes = len(points)
        edges = sorted([(abs(points[src][0] - points[dst][0]) + abs(points[src][1] - points[dst][1]), src, dst) for src in range(nodes) for dst in range(src + 1, nodes)])
        roots = [node for node in range(nodes)]

        def find(v):
            if roots[v] != v:
                roots[v] = find(roots[v])
            return roots[v]

        def union(u, v):
            (p1, p2) = (find(u), find(v))
            if p1 != p2:
                roots[p2] = roots[p1]
                return True
            return False
        return sum((distance for (distance, src, dst) in edges if union(src, dst)))
