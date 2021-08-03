class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c

            color[node] = c

            return all(dfs(n, c ^ 1) for n in graph[node])

        return all(dfs(n) for n in range(1, N + 1) if n not in color)
