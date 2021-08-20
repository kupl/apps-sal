class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if 0 == len(grid) - 1 and 0 == len(grid[0]) - 1:
            return 0
        (m, n) = (len(grid), len(grid[0]))
        seen = set()
        q = collections.deque()
        q.append((0, 0, k))
        seen.add((0, 0, k))
        steps = 0
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                (r, c, k) = q.popleft()
                for (x, y) in direction:
                    R = r + x
                    C = c + y
                    if (R, C, k) in seen:
                        continue
                    if R >= 0 and R < m and (C >= 0) and (C < n):
                        if k > 0 and grid[R][C] == 1 and ((R, C, k - 1) not in seen):
                            q.append((R, C, k - 1))
                            seen.add((R, C, k - 1))
                        if grid[R][C] == 0 and (R, C, k) not in seen:
                            if R == m - 1 and C == n - 1:
                                return steps + 1
                            q.append((R, C, k))
                            seen.add((R, C, k))
            steps += 1
        return -1
