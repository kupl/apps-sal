class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for (a, b) in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        colour = {}

        def dfs(node, c=0):
            if node in colour:
                return colour[node] == c
            colour[node] = c
            return all((dfs(nei, c ^ 1) for nei in graph[node]))
        return all((dfs(node) for node in range(1, N + 1) if node not in colour))
