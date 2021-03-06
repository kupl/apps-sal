from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([(0, 0, 0, k)])
        visited = set([(0, 0, k)])
        cur_min = -1
        while q:
            (row, col, dist, cur_k) = q.popleft()
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                if cur_min == -1:
                    return dist
            for (i, j) in directions:
                if row + i < len(grid) and row + i >= 0 and (col + j < len(grid[0])) and (col + j >= 0):
                    if (row + i, col + j, cur_k) not in visited and grid[row + i][col + j] == 0:
                        q.append((row + i, col + j, dist + 1, cur_k))
                        visited.add((row + i, col + j, cur_k))
                    if (row + i, col + j, cur_k - 1) not in visited and grid[row + i][col + j] == 1:
                        if cur_k > 0:
                            q.append((row + i, col + j, dist + 1, cur_k - 1))
                            visited.add((row + i, col + j, cur_k - 1))
        return cur_min
