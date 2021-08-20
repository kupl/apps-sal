class Solution:

    def minCostConnectPoints(self, A: List[List[int]], total=0) -> int:
        N = len(A)
        cand = set([i for i in range(N)])
        E = [[float('inf')] * N for _ in range(N)]
        for u in range(N):
            (x1, y1) = A[u]
            for v in range(u + 1, N):
                (x2, y2) = A[v]
                cost = abs(x1 - x2) + abs(y1 - y2)
                E[u][v] = cost
                E[v][u] = cost
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
        while len(cand):
            (cost, u) = heappop(q)
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
