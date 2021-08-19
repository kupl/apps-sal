class Solution:

    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        n = len(a)
        if n <= 1:
            return 0
        d = dict()
        q = []
        for i in range(n - 1):
            (xi, yi) = a[i]
            for j in range(n):
                (xj, yj) = a[j]
                val = abs(xi - xj) + abs(yi - yj)
                d[i, j] = val
                d[j, i] = val
                q.append((val, i, j))

        def union(u, v):
            UF[find(v)] = UF[find(u)]

        def find(u):
            if u != UF[u]:
                UF[u] = find(UF[u])
            return UF[u]
        UF = {i: i for i in range(n)}
        ans = set()
        heapify(q)
        cur = set([q[0][1], q[0][2]])
        cand = []
        for x in cur:
            for y in range(n):
                if y in cur:
                    continue
                cand.append((d[x, y], x, y))
        heapify(cand)
        ans = q[0][0]
        while len(cur) < n:
            (val, x, y) = heappop(cand)
            if find(x) != find(y):
                cur.add(y)
                union(x, y)
                ans += val
                for z in range(n):
                    if z in cur:
                        continue
                    heappush(cand, (d[y, z], y, z))
        return ans
