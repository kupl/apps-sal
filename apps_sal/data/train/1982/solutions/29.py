class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        dislike_graph = {}
        for i in range(1, N + 1):
            dislike_graph[i] = []
        for pair in dislikes:
            (a, b) = pair
            dislike_graph[a].append(b)
            dislike_graph[b].append(a)
        visited = [False] * (N + 1)
        color = {}

        def dfs(i):
            if visited[i]:
                return True
            visited[i] = True
            for nbs in dislike_graph[i]:
                if nbs in color:
                    if color[nbs] == color[i]:
                        return False
                else:
                    color[nbs] = -color[i]
                    if not dfs(nbs):
                        return False
            return True
        for i in range(1, N + 1):
            if visited[i]:
                continue
            color[i] = 1
            if not dfs(i):
                return False
        return True
