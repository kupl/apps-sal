class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def bfs(i):
            queue = collections.deque([(i, 0)])
            color[i] = 0
            while queue:
                person, c = queue.pop()
                for p in graph[person]:
                    if color[p] == c: return False
                    if color[p] == -1:
                        color[p] = 1 - c
                        queue.appendleft((p, 1 - c))
            return True
        
        graph = {i: [] for i in range(1, N + 1)}
        color = {i: -1 for i in range(1, N + 1)}
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(1, N + 1):
            if color[i] == -1 and not bfs(i): return False
        return True
