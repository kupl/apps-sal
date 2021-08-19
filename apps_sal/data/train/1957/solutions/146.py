class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (row, col) = (len(grid), len(grid[0]))
        q = collections.deque()
        q.append((0, 0, 0, k))
        visit = set()
        while q:
            (x, y, dist, k) = q.popleft()
            if x == row - 1 and y == col - 1:
                return dist
            if (x, y, k) in visit:
                continue
            visit.add((x, y, k))
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for (i, j) in dirs:
                if 0 <= x + i < row and 0 <= y + j < col:
                    if grid[x + i][y + j] == 0:
                        q.append((x + i, y + j, dist + 1, k))
                    elif grid[x + i][y + j] == 1 and k > 0:
                        q.append((x + i, y + j, dist + 1, k - 1))
        return -1
