class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for i in range(N)]
        for dislike in dislikes:
            graph[dislike[0] - 1].append(dislike[1] - 1)
            graph[dislike[1] - 1].append(dislike[0] - 1)

        visited = [False for i in range(N)]
        groups = [set([]), set([])]

        def dfs(root, group):
            groups[group].add(root)
            visited[root] = True
            for d in graph[root]:
                if d in groups[group]:
                    return False
                if not visited[d] and not dfs(d, 1 - group):
                    return False
            return True

        for i in range(N):
            if not visited[i] and not dfs(i, 0):
                return False
        return True
