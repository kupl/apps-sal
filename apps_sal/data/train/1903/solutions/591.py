# alright, whatever, time to solve it again in Python3 \\U0001f40d  whoo!

# ok silly mistake, but that's A ok :)

# alright! cool, well time for C++ then i'm done upsolving this one, it was fun :)

# class Solution:
#     def minCostConnectPoints(self, A: List[List[int]]) -> int:
#         N = len(A)
#         P = [i for i in range(N)]                       # \\U0001f642 parent representatives of N disjoint sets
#         E = []
#         for u in range(N):
#             x1, y1 = A[u]
#             for v in range(u + 1, N):
#                 x2, y2 = A[v]
#                 w = abs(x1 - x2) + abs(y1 - y2)
#                 E.append([ u, v, w ])                   # \\U0001f5fa edge u, v with weight w \\U0001f4b0
#         E.sort(key = lambda edge: edge[2])              # ⭐️ sort edges by weight w \\U0001f4b0
#         def find(x):
#             P[x] = P[x] if P[x] == x else find(P[x])
#             return P[x]
#         def union(a, b):
#             a = find(a)
#             b = find(b)
#             if a == b:
#                 return False
#             P[a] = b                                     # \\U0001f3b2 arbitrary choice
#             return True
#         return sum([w for u, v, w in E if union(u, v)])  # \\U0001f3af sum of minimum edge weights w \\U0001f4b0 to construct Kruskal's MST \\U0001f332

# create the edge cost lookups E
# create adjacency list adj
# create winner/best for each v


class Solution:
    def minCostConnectPoints(self, A: List[List[int]], total=0) -> int:
        N = len(A)
        # 1.
        cand = set([i for i in range(N)])
        E = [[float('inf')] * N for _ in range(N)]
        for u in range(N):
            x1, y1 = A[u]
            for v in range(u + 1, N):
                x2, y2 = A[v]
                cost = abs(x1 - x2) + abs(y1 - y2)
                E[u][v] = cost
                E[v][u] = cost
        # 2.
        q = []
        best = [float('inf') for _ in range(N)]
        winner = [-1 for _ in range(N)]
        s = 0
        cand.remove(0)
        for v in range(1, N):
            if best[v] > E[s][v]:
                best[v] = E[s][v]
                winner[v] = s
                heappush(q, [best[v], v])
        # 3.
        while len(cand):
            cost, u = heappop(q)
            if u not in cand:
                continue
            cand.remove(u)
            total += cost
            for v in range(N):
                if v not in cand:
                    continue
                if best[v] > E[u][v]:
                    best[v] = E[u][v]
                    winner[v] = u
                    heappush(q, [best[v], v])
        return total
