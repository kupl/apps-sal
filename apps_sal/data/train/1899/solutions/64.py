from collections import deque


class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:

        def get_edges(visited, A, i, j, isle):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            queue = deque([(i, j)])
            visited[i][j] = True
            edges = set()
            while queue:
                edge = 0
                (ci, cj) = queue.popleft()
                for (di, dj) in dirs:
                    x = ci + di
                    y = cj + dj
                    if 0 <= x < m and 0 <= y < n and (A[x][y] == 1) and (not visited[x][y]):
                        queue.append((x, y))
                        visited[x][y] = True
                    elif 0 <= x < m and 0 <= y < n and (A[x][y] == 0):
                        edge = 1
                if edge:
                    edges.add((ci, cj))
            return edges

        def manattan(a, b, c, d):
            return abs(a - c) + abs(b - d) - 1
        visited = [[0] * len(A[0]) for i in range(len(A))]
        m = len(A)
        n = len(A[0])
        edge_islands = []
        counts = 0
        for ii in range(m):
            for jj in range(n):
                if A[ii][jj] == 1 and (not visited[ii][jj]):
                    counts += 1
                    edge_islands.append(get_edges(visited, A, ii, jj, counts))
        isle1 = edge_islands[0]
        isle2 = edge_islands[1]
        mins = float('inf')
        for i1 in isle1:
            for i2 in isle2:
                mins = min(mins, manattan(i1[0], i1[1], i2[0], i2[1]))
        return mins
