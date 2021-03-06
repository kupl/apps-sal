from heapq import heappop, heappush


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return -1
        deltas = ((-1, 0), (0, 1), (0, -1), (1, 0))
        (n, m) = (len(grid), len(grid[0]))
        (source, target) = ((0, 0), (n - 1, m - 1))
        queue = deque([(0, source, 0)])
        seen = {source: 0}
        while queue:
            (usedK, currPos, steps) = queue.popleft()
            if currPos == target:
                return steps
            for (delta_x, delta_y) in deltas:
                (x, y) = (currPos[0] + delta_x, currPos[1] + delta_y)
                if x >= 0 and x < n and (y >= 0) and (y < m):
                    if (x, y) not in seen or seen[x, y] > usedK:
                        if grid[x][y] == 0:
                            seen[x, y] = usedK
                            queue.append((usedK, (x, y), steps + 1))
                        elif usedK < k:
                            seen[x, y] = usedK + 1
                            queue.append((usedK + 1, (x, y), steps + 1))
        return -1
