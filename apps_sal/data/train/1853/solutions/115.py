class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = collections.defaultdict(dict)
        for (i, j, w) in edges:
            g[i][j] = w
            g[j][i] = w
        t = distanceThreshold

        def dist(u):
            q = [(0, u)]
            ret = {}
            while q:
                (d, v) = heapq.heappop(q)
                if v in ret:
                    continue
                ret[v] = d
                for k in g[v]:
                    if k not in ret and d + g[v][k] <= t:
                        heapq.heappush(q, (d + g[v][k], k))
            return len(ret)
        ans = None
        num = n + 1
        for i in range(n):
            c = dist(i)
            if c <= num:
                num = c
                ans = i
        return ans
