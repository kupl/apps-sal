"""



"""
from collections import deque


class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0]) if rows else 0
        if not rows or not cols:
            return -1
        self.queue = deque()
        self.visited = set()

        def floodFill(A, row, col, rows, cols):
            if not (0 <= row < rows and 0 <= col < cols):
                return
            if not A[row][col] or (row, col) in self.visited:
                return
            A[row][col] = 2
            self.queue.append((row, col, 0))
            self.visited.add((row, col))
            floodFill(A, row + 1, col, rows, cols)
            floodFill(A, row - 1, col, rows, cols)
            floodFill(A, row, col + 1, rows, cols)
            floodFill(A, row, col - 1, rows, cols)
        flood_fill = False
        for row in range(rows):
            for col in range(cols):
                if A[row][col] == 1:
                    flood_fill = True
                    floodFill(A, row, col, rows, cols)
                    break
            if flood_fill:
                break
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while len(self.queue):
            (top_r, top_c, dist) = self.queue.popleft()
            for (d_r, d_c) in directions:
                n_r = top_r + d_r
                n_c = top_c + d_c
                if 0 <= n_r < rows and 0 <= n_c < cols and ((n_r, n_c) not in self.visited):
                    if A[n_r][n_c] == 0:
                        self.queue.append((n_r, n_c, dist + 1))
                        self.visited.add((n_r, n_c))
                    elif A[n_r][n_c] == 1:
                        return dist
        return -1
