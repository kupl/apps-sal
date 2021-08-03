class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        q = [(0, 0, 0, k)]
        seen = {}
        while len(q) > 0:
            i, j, steps, quota = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue

            if grid[i][j] == 1:
                quota -= 1

            if quota == -1:
                continue

            if i + 1 == R and j + 1 == C:
                return steps

            key = (i, j, quota)
            if key in seen:
                continue
            seen[key] = steps

            q.append((i - 1, j, steps + 1, quota))
            q.append((i + 1, j, steps + 1, quota))
            q.append((i, j - 1, steps + 1, quota))
            q.append((i, j + 1, steps + 1, quota))

        return -1
