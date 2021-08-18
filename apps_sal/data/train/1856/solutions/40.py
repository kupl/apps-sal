class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        queue = deque()

        queue.append([0, 0, 0, 0])

        visited = {(0, 0, 0): 1}
        n = len(grid)

        while(len(queue) > 0):

            x, y, dic, step = queue.popleft()
            if x == n - 1 and y == n - 2 and dic == 0:
                return step

            if dic == 0:
                nx, ny = x, y + 1
                if nx >= 0 and nx < n and ny >= 0 and ny + 1 < n:
                    if grid[nx][ny + 1] == 0 and (nx, ny, 0) not in visited:
                        queue.append([nx, ny, 0, step + 1])
                        visited[(nx, ny, 0)] = 1

                nx, ny = x, y
                checkx1, checky1 = x + 1, y
                checkx, checky = x + 1, y + 1
                if checkx1 >= 0 and checkx1 < n and checky1 >= 0 and checky1 < n:
                    if checkx >= 0 and checkx < n and checky >= 0 and checky < n:
                        if grid[checkx1][checky1] == 0 and grid[checkx][checky] == 0 and (nx, ny, 1) not in visited:
                            queue.append([nx, ny, 1, step + 1])
                            visited[(nx, ny, 1)] = 1

                        if grid[checkx1][checky1] == 0 and grid[checkx][checky] == 0 and (checkx1, checky1, 0) not in visited:
                            queue.append([checkx1, checky1, 0, step + 1])
                            visited[(checkx1, checky1, 0)] = 1

            if dic == 1:
                nx, ny = x + 1, y
                if nx >= 0 and nx + 1 < n and ny >= 0 and ny < n:
                    if grid[nx + 1][ny] == 0 and (nx, ny, 1) not in visited:
                        queue.append([nx, ny, 1, step + 1])
                        visited[(nx, ny, 1)] = 1

                nx, ny = x, y
                checkx1, checky1 = x, y + 1
                checkx, checky = x + 1, y + 1
                if checkx1 >= 0 and checkx1 < n and checky1 >= 0 and checky1 < n:
                    if checkx >= 0 and checkx < n and checky >= 0 and checky < n:
                        if grid[checkx1][checky1] == 0 and grid[checkx][checky] == 0 and (nx, ny, 0) not in visited:
                            queue.append([nx, ny, 0, step + 1])
                            visited[(nx, ny, 0)] = 1
                        if grid[checkx1][checky1] == 0 and grid[checkx][checky] == 0 and (x, y + 1, 1) not in visited:
                            queue.append([x, y + 1, 1, step + 1])
                            visited[(x, y + 1, 1)] = 1
        return -1
