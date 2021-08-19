class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = set()
        visited.add((0, 0, k))
        candidates = collections.deque([])
        candidates.append((0, 0, 0, k))
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        while len(candidates) > 0:
            (ci, cj, steps, ck) = candidates.popleft()
            if ci == len(grid) - 1 and cj == len(grid[0]) - 1:
                return steps
            for (x, y) in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                (ni, nj) = (ci + x, cj + y)
                if ni < 0 or nj < 0 or ni >= len(grid) or (nj >= len(grid[0])):
                    continue
                if (ni, nj, ck) in visited:
                    continue
                if grid[ni][nj] == 1 and ck > 0:
                    candidates.append((ni, nj, steps + 1, ck - 1))
                    visited.add((ni, nj, ck))
                elif grid[ni][nj] == 0:
                    candidates.append((ni, nj, steps + 1, ck))
                    visited.add((ni, nj, ck))
        return -1
