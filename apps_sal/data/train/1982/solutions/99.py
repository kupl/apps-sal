class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(N)]
        for pair in dislikes:
            graph[pair[0] - 1].append(pair[1] - 1)
            graph[pair[1] - 1].append(pair[0] - 1)
        visited = {}

        def dfs(node, color):
            nonlocal visited
            visited[node] = color
            for child in graph[node]:
                if not child in visited:
                    if not dfs(child, not color):
                        return False
                elif visited[child] == color:
                    return False
            return True
        for i in range(N):
            if not i in visited:
                if not dfs(i, False):
                    return False
        return True
