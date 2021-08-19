from queue import PriorityQueue


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = []
        N = len(points)

        for i in range(N):
            for j in range(i + 1, N):
                a, b = points[i]
                c, d = points[j]
                dist = abs(a - c) + abs(b - d)
                q.append((dist, i, j))

        heapify(q)
        ans = 0
        par = list(range(N))
        rank = [0] * N

        def find_parent(a):
            if par[a] == a:
                return a
            par[a] = find_parent(par[a])
            return par[a]

        def join(a, b):
            pa, pb = find_parent(a), find_parent(b)
            if pa == pb:
                return 0
            # Attach smaller rank tree under root of
            # high rank tree (Union by Rank)
            if rank[pa] < rank[pb]:
                par[pa] = pb
            elif rank[pa] > rank[pb]:
                par[pb] = pa
            # If ranks are same, then make one as root
            # and increment its rank by one
            else:
                par[pb] = pa
                rank[pa] += 1
            return 1

        while q:
            dist, i, j = heappop(q)
            if join(i, j):
                ans += dist

        return ans
