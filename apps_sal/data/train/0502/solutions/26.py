class Solution:
    def minMalwareSpread(self, graph, initial):
        def dfs(node, visited):
            if node in initial:
                return 0
            visited.add(node)
            res = 1
            for nxt_node, v in enumerate(graph[node]):
                if v == 0 or nxt_node == node:
                    continue
                if nxt_node not in visited:
                    sub = dfs(nxt_node, visited)
                    if sub == 0:
                        return 0
                    res += sub
            return res

        initial = set(initial)
        res = [-1, 0]
        for n in list(initial):
            initial.discard(n)
            res = max([dfs(n, set()), -n], res)
            initial.add(n)
        return -res[1]

    def minMalwareSpread_I(self, graph, initial):
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            parents[find(x)] = find(y)
        n = len(graph)
        parents = list(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] == 1:
                    union(i, j)
        area = collections.Counter(find(i) for i in range(n))
        malware = collections.Counter(find(i) for i in initial)
        return min(initial, key=lambda i: [(malware[find(i)] == 1) * -area[find(i)], i])

    def minMalwareSpread_II(self, graph: List[List[int]], initial: List[int]) -> int:
        union_mem = {i: i for i in range(len(graph))}
        count = collections.Counter(range(len(graph)))

        def find(vertex):
            if union_mem[vertex] != vertex:
                union_mem[vertex] = find(union_mem[vertex])
            return union_mem[vertex]

        def union(v1, v2):
            v1f, v2f = find(v1), find(v2)
            if v1f != v2f:
                count[v1f] += count[v2f]
                union_mem[v2f] = v1f

        N = len(graph)
        for r in range(N):
            for c in range(N):
                if r != c and graph[r][c] == 1:
                    union(r, c)
        groups = collections.defaultdict(list)
        for v1 in initial:
            v1f = find(v1)
            groups[v1f].append(v1)
        return -max(([count[find(v1)], -v1] for v1 in initial if len(groups[find(v1)]) == 1), default=[0, -min(initial)])[1]
