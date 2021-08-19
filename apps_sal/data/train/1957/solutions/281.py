from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(i, j):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
                return True
            return False

        dq = deque([(0, 0, k, 0)])
        visited = {}
        res = math.inf

        def search(i, j, k, l):
            nonlocal res
            if l >= res:
                return False
            if (i, j) in visited and visited[(i, j)] >= k:
                return False
            visited[(i, j)] = k if (i, j) not in visited else max(k, visited[(i, j)])

            if k < 0:
                return False
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                res = l
                return True
            # shortcut(只有(i,j) not in visited才能保证前面也是最短路径)
            if len(grid) - 1 - i + len(grid[0]) - 1 - j <= k + 1:
                res = min(res, l + len(grid) - 1 - i + len(grid[0]) - 1 - j)
                if (i, j) not in visited:
                    return True
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if valid(i + di, j + dj):
                    next_k = k if grid[i + di][j + dj] == 0 else k - 1
                    dq.append((i + di, j + dj, next_k, l + 1))

            return False
        while dq:
            i, j, k, l = dq.popleft()
            if search(i, j, k, l):
                break
        return res if res != math.inf else -1
