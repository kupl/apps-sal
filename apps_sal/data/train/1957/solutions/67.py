class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # BFS wth obstacle elimination

        # when should u add the visited?? eg. test case.   0 1 0 1
        # 0 0 1 0

        queue = []
        queue.append((0, 0, 0, 0))  # i,j,obstacles used, distance
        visited = set()
        visited.add((0, 0, 0))  # i, j, obstacles used

        while queue:
            i, j, obstacles_used, length = queue.pop(0)
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return length  # because of the stpid base case [[0]]

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for a, b in directions:
                newi = i + a
                newj = j + b
                if newi >= 0 and newi < len(grid) and newj >= 0 and newj < len(grid[0]):
                    newObstacles = obstacles_used + grid[newi][newj]
                    # if newi == len(grid)-1 and newj == len(grid[0])-1 and newObstacles <=k:
                    #     return length + 1
                    if newObstacles <= k and (newi, newj, newObstacles) not in visited:
                        visited.add((newi, newj, newObstacles))
                        queue.append((newi, newj, newObstacles, length + 1))

        return -1
