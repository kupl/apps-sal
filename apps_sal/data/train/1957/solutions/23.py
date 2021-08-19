import collections


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = collections.deque([(0, 0, k)])
        seen = set([(0, 0, k)])
        level = 0
        while queue:
            #print(queue, seen)
            size = len(queue)
            for _ in range(size):
                x, y, remain = queue.popleft()
                if x == m - 1 and y == n - 1:
                    return level
                for dx, dy in move:
                    newX, newY = x + dx, y + dy
                    if 0 <= newX < m and 0 <= newY < n:
                        if grid[newX][newY] == 0:
                            if (newX, newY, remain) not in seen:
                                queue.append((newX, newY, remain))
                                seen.add((newX, newY, remain))
                        else:
                            if remain > 0:
                                if (newX, newY, remain - 1) not in seen:
                                    queue.append((newX, newY, remain - 1))
                                    seen.add((newX, newY, remain - 1))
            level += 1
        return -1
