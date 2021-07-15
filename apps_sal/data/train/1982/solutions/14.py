import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(curr, curr_color):
            color[curr] = curr_color
            for next in graph[curr]:
                if color[next] == None:
                    dfs(next, not curr_color)
                elif color[next] == curr_color:
                    return False
            return True
        
        graph = collections.defaultdict(list)
        color = [None] * (N + 1)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        for n in range(1, N + 1):
            if color[n] == None:
                if not dfs(n, True):
                    return False
        return True
