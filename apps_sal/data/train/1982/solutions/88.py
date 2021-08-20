class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        for (x, y) in dislikes:
            graph[x].add(y)
            graph[y].add(x)
        color = {}

        def dfs(x, c=0):
            if x in color:
                return color[x] == c
            color[x] = c
            return all((dfs(nei, c ^ 1) for nei in graph[x]))
        return all((dfs(x) for x in range(1, N + 1) if x not in color))
