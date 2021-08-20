class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        def bfs(n):
            q = [(n, 1)]
            while q:
                (x, color) = q.pop()
                state[x] = color
                for i in graph[x]:
                    if state[i] == 0:
                        q.append((i, -color))
                    if state[i] == color:
                        return False
            return True
        graph = [set() for _ in range(N + 1)]
        for (a, b) in dislikes:
            graph[a - 1].add(b - 1)
            graph[b - 1].add(a - 1)
        state = [0] * N
        for i in range(N):
            if state[i] != 0:
                continue
            if not bfs(i):
                return False
        return True
