class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degree = dict()
        for (i, node) in enumerate(graph):
            degree[i] = len(node)
            for n in node:
                adj[n].append(i)
        bfs = deque([x for (x, count) in degree.items() if count == 0])
        result = []
        while bfs:
            current = bfs.popleft()
            result.append(current)
            for n in adj[current]:
                degree[n] -= 1
                if degree[n] == 0:
                    bfs.append(n)
        return sorted(result)
