from collections import deque


class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:

        def color(x, y):
            dfs = [(x, y)]
            while dfs:
                (a, b) = dfs.pop()
                A[a][b] = 2
                for (mx, my) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= a + mx < len(A) and 0 <= b + my < len(A[0]):
                        if A[a + mx][b + my] == 1:
                            dfs.append((a + mx, b + my))

        def firstOne():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j]:
                        color(i, j)
                        return (i, j)
        point = firstOne()
        self.best = 1000

        def findClosest(point):
            visited = {}
            bfs = deque([(point, 0)])
            while bfs:
                (curr, dist) = bfs.popleft()
                if curr in visited:
                    if visited[curr] <= dist:
                        continue
                visited[curr] = dist
                for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    cx = curr[0] + x
                    cy = curr[1] + y
                    if 0 <= cx < len(A) and 0 <= cy < len(A[0]):
                        if A[cx][cy] == 2:
                            bfs.append(((cx, cy), 0))
                        elif A[cx][cy] == 1:
                            self.best = min(self.best, dist)
                        else:
                            bfs.append(((cx, cy), dist + 1))
        findClosest(point)
        return self.best
