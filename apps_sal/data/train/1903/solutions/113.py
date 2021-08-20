from heapq import heapify, heappop, heappush


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                l = dist(points[i], points[j])
                edges.append((i, j, l))

        def prim(nodes, edges):
            conn = defaultdict(list)
            for (n1, n2, c) in edges:
                conn[n1].append((c, n1, n2))
                conn[n2].append((c, n2, n1))
            mst = []
            used = set([nodes[0]])
            usable_edges = conn[nodes[0]][:]
            heapify(usable_edges)
            ans = 0
            while usable_edges:
                (cost, n1, n2) = heappop(usable_edges)
                if n2 not in used:
                    used.add(n2)
                    mst.append((n1, n2, cost))
                    ans += cost
                    for e in conn[n2]:
                        if e[2] not in used:
                            heappush(usable_edges, e)
            return ans
        nodes = list(range(n))
        return prim(nodes, edges)
