class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        length, width = len(grid), len(grid[0])
        # (l,w,steps,k)
        que = collections.deque([])
        que.append((0, 0, 0, k))
        visited = set()
        visited.add((0, 0, k))
        directions = ([-1, 0], [0, 1], [1, 0], [0, -1])
        while len(que):
            x, y, steps, eliminates = que.popleft()
            # BFS 保证第一个visit是steps最少的
            if x == length - 1 and y == width - 1:
                return steps
            for dx, dy in directions:
                next_x = x + dx
                next_y = y + dy
                if self.isValid(next_x, next_y, grid) and (next_x, next_y, eliminates) not in visited:
                    if grid[next_x][next_y] == 1 and eliminates > 0:
                        visited.add((next_x, next_y, eliminates))
                        que.append((next_x, next_y, steps + 1, eliminates - 1))
                    elif grid[next_x][next_y] == 0:
                        visited.add((next_x, next_y, eliminates))
                        que.append((next_x, next_y, steps + 1, eliminates))
        return -1

    def isValid(self, next_x, next_y, grid):
        if next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]):
            return True
        else:
            return False
