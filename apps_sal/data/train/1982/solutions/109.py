class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edges = {ii: [] for ii in range(1, N + 1)}
        for (ii, jj) in dislikes:
            edges[ii].append(jj)
            edges[jj].append(ii)
        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all([dfs(ii, c ^ 1) for ii in edges[node]])
        return all([dfs(ii) for ii in range(1, N + 1) if ii not in color])
