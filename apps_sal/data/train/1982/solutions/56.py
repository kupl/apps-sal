from collections import defaultdict


class Solution:
    def possibleBipartition(self, N, dislikes):
        graph = defaultdict(set)
        for u, v in dislikes:
            graph[u].add(v)
            graph[v].add(u)
        color = dict()

        def dfs(node):
            for nei in graph[node]:
                if nei in color:
                    if color[nei] == color[node]:
                        return False
                else:
                    color[nei] = color[node] ^ 1
                    if not dfs(nei):
                        return False
            return True
        for node in range(1, N + 1):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False
        return True

# class Solution:
#     def possibleBipartition(self, N, dislikes):
#         graph = [[] for _ in range(N+1)]
#         for u, v in dislikes:
#             graph[u].append(v)
#             graph[v].append(u)
#         color = dict()
#         def dfs(node):
#             for nei in graph[node]:
#                 if nei in color:
#                     if color[nei] == color[node]:
#                         return False
#                 else:
#                     color[nei] = color[node] ^ 1
#                     if not dfs(nei):
#                         return False
#             return True
#         for node in range(1, N+1):
#             if node not in color:
#                 color[node] = 0
#                 if not dfs(node):
#                     return False
#         return True
