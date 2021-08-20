from collections import deque


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for i in range(N)]
        for (a, b) in dislikes:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        color_array = [-1] * N
        queue = deque()
        for i in range(N):
            if color_array[i] == -1:
                color_array[i] = 1
                queue.append(i)
                while queue:
                    u = queue.popleft()
                    for i in adj[u]:
                        if color_array[i] == -1:
                            color_array[i] = 1 - color_array[u]
                            queue.append(i)
                        elif color_array[u] == color_array[i]:
                            return False
        return True
