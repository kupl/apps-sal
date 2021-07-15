import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(curr, current_color):
            color[curr] = current_color
            for next in graph[curr]:
                if color[next] == None:
                    dfs(next, not current_color)
                elif color[next] == current_color:
                    return False
            return True

        color = [None] * (N + 1)
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        for n in range(1, N + 1):
            if color[n] == None:
                if not dfs(n, True):
                    return False
        return True
