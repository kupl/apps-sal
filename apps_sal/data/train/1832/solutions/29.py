class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = collections.defaultdict(dict)
        for edge in edges:
            u, v, w = edge
            g[u][v] = w
            g[v][u] = w

        pq = [(-M, 0)]
        HP = {}
        while pq:
            hp, node = heapq.heappop(pq)
            hp = -hp
            if node in HP:
                continue
            HP[node] = hp
            for child in g[node]:
                if child not in HP and hp - g[node][child] - 1 >= 0:
                    heapq.heappush(pq, (-(hp - g[node][child] - 1), child))

        res = len(HP)
        for edge in edges:
            u, v = edge[0], edge[1]
            uv = HP[u] if u in HP else 0
            vu = HP[v] if v in HP else 0
            res += min(edge[2], uv + vu)
        return res
