class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edge_set = set(tuple(x) for x in edges)

        graphs = [defaultdict(list) for i in range(3)]
        for e in edges:
            graphs[e[0] - 1][e[1]].append(e[2])
            graphs[e[0] - 1][e[2]].append(e[1])
            if e[0] == 3:
                for k in [0, 1]:
                    graphs[k][e[1]].append(e[2])
                    graphs[k][e[2]].append(e[1])

        def ct_ccmp(g):
            visited = dict()
            q = deque()
            nt = 0
            for i in range(1, n + 1):
                if i in visited:
                    continue
                if len(g[i]) > 0:
                    q.append(i)
                    visited[i] = nt
                    while len(q) > 0:
                        cur = q.popleft()
                        for x in g[cur]:
                            if x in visited:
                                continue
                            q.append(x)
                            visited[x] = nt
                nt += 1
            return nt

        if ct_ccmp(graphs[0]) > 1 or ct_ccmp(graphs[1]) > 1:
            return -1

        nt = ct_ccmp(graphs[2])
        return len(edges) - (n - nt) - 2 * (nt - 1)
