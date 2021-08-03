class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return int()

        queue = collections.deque([(0, 0, 0, 0)])
        row, col = len(grid), len(grid[0])
        visited = set()

        while queue:
            x, y, obstacle, path = queue.popleft()

            for i, j in (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < row and 0 <= j < col:
                    if grid[i][j] == 1 and obstacle < k and (i, j, obstacle + 1) not in visited:
                        visited.add((i, j, obstacle + 1))
                        queue.append((i, j, obstacle + 1, path + 1))
                    elif grid[i][j] == 0 and (i, j, obstacle) not in visited:
                        if i == row - 1 and j == col - 1:
                            return path + 1
                        visited.add((i, j, obstacle))
                        queue.append((i, j, obstacle, path + 1))

        return -1
