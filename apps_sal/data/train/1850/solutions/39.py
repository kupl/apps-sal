class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * N
        graph = defaultdict(set)
        for (u, v) in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = {}
        return [self.dfs(graph, i, -1, visited)[0] for i in range(N)]

    def dfs(self, graph, node, parent, visited):
        if (node, parent) in visited:
            return visited[node, parent]
        (distance, count) = (0, 1)
        for child in graph[node]:
            if child != parent:
                (d, c) = self.dfs(graph, child, node, visited)
                distance += d + c
                count += c
        visited[node, parent] = (distance, count)
        return (distance, count)
