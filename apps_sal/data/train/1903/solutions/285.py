class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N <= 1:
            return 0
        edges = []
        for i in range(N):
            p1 = points[i]
            for j in range(i + 1, N):
                p2 = points[j]
                cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                edges.append((cost, i, j))
        edges.sort()
        A = set()
        B = set(range(N))
        A.add(0)
        B.discard(0)
        rtv = 0
        while len(B) > 0:
            for (idx, e) in enumerate(edges):
                (c, a, b) = e
                if a in A and b in B:
                    B.discard(b)
                    A.add(b)
                    rtv += c
                    edges.pop(idx)
                    break
                elif b in A and a in B:
                    B.discard(a)
                    A.add(a)
                    rtv += c
                    edges.pop(idx)
                    break
        return rtv
