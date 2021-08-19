class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        N = len(A)
        P = [i for i in range(N)]                        # \\U0001f642 parent representatives of N disjoint sets
        E = []
        for u in range(N):
            x1, y1 = A[u]
            for v in range(u + 1, N):
                x2, y2 = A[v]
                w = abs(x1 - x2) + abs(y1 - y2)
                E.append([u, v, w])                    # \\U0001f5fa edge u, v with weight w \\U0001f4b0
        E.sort(key=lambda edge: edge[2])               # ⭐️ sort edges by weight w \\U0001f4b0

        def find(x):
            P[x] = P[x] if P[x] == x else find(P[x])
            return P[x]

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            P[a] = b                                     # \\U0001f3b2 arbitrary choice
            return True
        return sum([w for u, v, w in E if union(u, v)])  # \\U0001f3af sum of minimum edge weights w \\U0001f4b0 to construct Kruskal's MST \\U0001f332
