class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        nei = [[] for _ in range(n + 1)]
        for t, u, v in edges:
            nei[u].append([-t, v])
            nei[v].append([-t, u])
        h = [[-3, 1]]
        v = [set() for _ in range(2)]
        cnt = -1
        while h:
            t, p = heappop(h)
            if t == -3:
                if any(p not in i for i in v):
                    cnt += 1
                    for i in v:
                        i.add(p)
                    for q in nei[p]:
                        heappush(h, q)
            else:
                if p not in v[-t - 1]:
                    cnt += 1
                    v[-t - 1].add(p)
                    for q in nei[p]:
                        heappush(h, q)
        return len(edges) - cnt if all(len(i) == n for i in v) else -1
