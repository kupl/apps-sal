class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])

        def labelIsland(i, j):
            stack = [(i, j)]
            visited = {(i, j)}
            while stack:
                x, y = stack.pop()
                A[x][y] = 2
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                        if A[nx][ny] == 1:
                            visited.add((nx, ny))
                            stack.append((nx, ny))
            return visited

        def bfs(source) -> int:
            queue = collections.deque([(0, x[0], x[1]) for x in source])
            visited = source
            ans = math.inf
            while queue:
                dist, x, y = queue.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                        if A[nx][ny] == 1:
                            return dist
                        else:
                            visited.add((nx, ny))
                            queue.append((dist + 1, nx, ny))
            return ans

        ans = math.inf
        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    source = labelIsland(i, j)
                    return bfs(source)
