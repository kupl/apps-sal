class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        graph = {}
        for Type, start, end in edges:
            if start not in graph:
                graph[start] = []
            if end not in graph:
                graph[end] = []

            graph[start].append([Type, end])
            graph[end].append([Type, start])

        def dfs(node, p):
            for Type, neighbour in graph[node]:
                if Type in p:
                    if neighbour not in visited:
                        visited[neighbour] = True
                        dfs(neighbour, p)

        visited = {}
        dfs(1, [1, 3])
        if len(list(visited.keys())) != n:
            return -1

        visited = {}
        dfs(1, [2, 3])
        if len(list(visited.keys())) != n:
            return -1

        visited = {}
        blue_cc = 0
        blue_edges = 0
        for Type, start, end in edges:
            if Type == 3:

                if start not in visited:
                    temp = len(list(visited.keys()))
                    blue_cc += 1
                    dfs(start, [3])
                    blue_edges += len(list(visited.keys())) - temp - 1

                if end not in visited:
                    temp = len(list(visited.keys()))
                    blue_cc += 1
                    dfs(end, [3])
                    blue_edges += len(list(visited.keys())) - temp - 1

        unvisited = len(list(graph.keys())) - len(list(visited.keys()))

        print((blue_edges, unvisited, blue_cc))
        return len(edges) - (blue_edges + 2 * unvisited + 2 * (blue_cc - 1))
