class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        queue = []
        queue.append((0, 0, 0, 0))
        visited = set()
        visited.add((0, 0, 0))

        while queue:
            i, j, obstacles_used, length = queue.pop(0)
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return length

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for a, b in directions:
                newi = i + a
                newj = j + b
                if newi >= 0 and newi < len(grid) and newj >= 0 and newj < len(grid[0]):
                    newObstacles = obstacles_used + grid[newi][newj]
                    if newObstacles <= k and (newi, newj, newObstacles) not in visited:
                        visited.add((newi, newj, newObstacles))
                        queue.append((newi, newj, newObstacles, length + 1))

        return -1
