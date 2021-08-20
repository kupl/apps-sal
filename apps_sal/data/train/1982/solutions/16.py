class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        coloring = {i: -1 for i in range(1, N + 1)}
        edges = defaultdict(list)
        for (a, b) in dislikes:
            edges[a].append(b)
            edges[b].append(a)

        def dfs(node, color):
            if coloring[node] != -1:
                return coloring[node] == color
            coloring[node] = color
            for hater in edges[node]:
                if not dfs(hater, 1 - color):
                    return False
            return True
        return all([coloring[node] != -1 or dfs(node, 0) for node in range(1, N + 1)])
