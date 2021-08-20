from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([(0, 0, k, 0)])
        rows = len(grid)
        cols = len(grid[0])
        ans = float('inf')
        vis = {(0, 0, k): 1}
        while len(queue) > 0:
            (x, y, rem, depth) = queue.popleft()
            if x == rows - 1 and y == cols - 1:
                return depth
            for (i, j) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                i += x
                j += y
                if i < 0 or i >= rows or j < 0 or (j >= cols) or ((i, j, rem) in vis) or (grid[i][j] == 1 and rem <= 0):
                    continue
                elif grid[i][j] == 0 and (i, j, rem) not in vis:
                    vis[i, j, rem] = 1
                    queue.append((i, j, rem, depth + 1))
                elif grid[i][j] == 1 and rem > 0 and ((i, j, rem - 1) not in vis):
                    vis[i, j, rem - 1] = 1
                    queue.append((i, j, rem - 1, depth + 1))
        if ans == float('inf'):
            return -1
        return ans
