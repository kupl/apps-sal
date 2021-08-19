class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # traverse upper left to lower right
        # double for loop
        # visited = [[0 for x in row] for row in grid]
        # don't use visited grid, use viisted set that keeps track of remaining obstacles instead.

        # obstacles = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 0: #and visited[i][j] != 1:
        #             # self.traverse(i,j, grid, visited, k)
        #             continue
        #         else:
        #             obstacles.append((i,j))

        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        queue.append((0, 0, k, 0))
        # need to keep track of number of steps. put it in the tuple alongside the coordinates
        visited = set((0, 0, k))
        count = 0
        while queue:
            x, y, obstacles, steps = queue.popleft()
            visited.add((x, y, obstacles))

            for dx, dy in directions:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                    if grid[x + dx][y + dy] == 0 and (x + dx, y + dy, obstacles) not in visited:
                        if x + dx == len(grid) - 1 and y + dy == len(grid[0]) - 1:
                            return steps + 1
                        queue.append((x + dx, y + dy, obstacles, steps + 1))
                        visited.add((x + dx, y + dy, obstacles))

                    if grid[x + dx][y + dy] == 1 and obstacles > 0 and (x + dx, y + dy, obstacles - 1) not in visited:
                        queue.append((x + dx, y + dy, obstacles - 1, steps + 1))
                        visited.add((x + dx, y + dy, obstacles - 1))

        return -1
