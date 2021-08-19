from collections import deque
from typing import List


class Solution:

    def getNeighbors(self, width, height, node):
        (row, column) = node
        for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            (rr, cc) = (row + dr, column + dc)
            if 0 <= rr < height and 0 <= cc < width:
                yield (rr, cc)

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (height, width) = (len(grid), len(grid[0]))
        queue = deque()
        queue.append(((0, 0), k))
        (result, visited) = (0, set())
        visited.add(((0, 0), k))
        while queue:
            length = len(queue)
            for _ in range(length):
                (node, remove_capacity) = queue.popleft()
                if node == (height - 1, width - 1):
                    return result
                for (rr, cc) in self.getNeighbors(width, height, node):
                    capacity = remove_capacity - grid[rr][cc]
                    key = ((rr, cc), capacity)
                    if key not in visited and capacity >= 0:
                        queue.append(key)
                        visited.add(key)
            result += 1
        return -1
