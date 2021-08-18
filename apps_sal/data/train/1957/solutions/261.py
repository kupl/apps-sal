class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return -1
        if m == 1 and n == 1:
            return 0
        di = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def get_nei(i, j):
            return [(i + x, j + y) for (x, y) in di if 0 <= i + x <= m - 1 and 0 <= j + y <= n - 1]

        seen = {(0, 0): 0}
        seen2 = {(0, 0): k}
        q = collections.deque()
        q.append((0, 0, k, 0))
        while q:
            i, j, ob, depth = q.popleft()
            for x, y in get_nei(i, j):
                cob = ob
                if x == m - 1 and y == n - 1 and cob >= 0:
                    return depth + 1
                if grid[x][y] == 1:
                    cob -= 1
                    if cob < 0:
                        continue
                if (x, y) in seen and seen[(x, y)] <= depth + 1 and seen2[(x, y)] >= cob:
                    continue
                seen[(x, y)] = depth + 1
                seen2[(x, y)] = cob
                q.append((x, y, cob, depth + 1))
        return -1
