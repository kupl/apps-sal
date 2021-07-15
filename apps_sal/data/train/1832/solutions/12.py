class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = collections.defaultdict(dict)
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w
        q = [(0, 0)]
        visited = [10 ** 9 + 1 for i in range(N)]
        visited[0] = 0
        result = 0
        edges2 = {}
        while q:
            m, u = heapq.heappop(q)
            if m > visited[u]:
                continue
            result += 1
            for v, w in list(g[u].items()):
                edge = (min(u, v), max(u, v))
                l = None
                if edge not in edges2:
                    l = edges2[edge] = [0, 0]
                else:
                    l = edges2[edge]
                i = 0 if u < v else 1
                l[i] = max(l[i], min(w, M - m))
                mm = m + w + 1
                if mm <= M and mm < visited[v]:
                    visited[v] = mm
                    heapq.heappush(q, (mm, v))
        
        for (u, v), (l1, l2) in list(edges2.items()):
            result += min(l1 + l2, g[u][v])
        return result

