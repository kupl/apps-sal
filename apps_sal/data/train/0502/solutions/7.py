class Solution:
    def minMalwareSpread(self, graph, initial):
        def dfs(i):
            nodes.add(i)
            for j in range(len(graph[i])):
                if graph[i][j] and j not in nodes:
                    dfs(j)
        rank = {}
        initial = set(initial)
        for node in sorted(initial):
            nodes = set()
            dfs(node)
            rank[node] = nodes
        print(rank)

        passed = []
        for k, v in list(rank.items()):
            count = 0
            for i in initial:
                if i in v:
                    count += 1
            if count <= 1:
                passed.append((k, len(v)))
        passed.sort(key=lambda x: x[1], reverse=True)
        if len(passed) == 0:
            return min(initial)
        else:
            return passed[0][0]
