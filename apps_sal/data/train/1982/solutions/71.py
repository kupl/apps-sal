def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n

    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            stack = [start]

            while stack:
                parent = stack.pop()

                for child in graph[parent]:
                    if color[child] == -1:
                        color[child] = 1 - color[parent]
                        stack.append(child)
                    elif color[parent] == color[child]:
                        return False

    return True

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(N)]
        for u, v in dislikes:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        return is_bipartite(graph)
