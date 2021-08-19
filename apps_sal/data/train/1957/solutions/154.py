class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Just use BFS to record the steps and celss modified
        # One concern is that you cannot simply record the stepped cells
        # Because if u stepped on one cell u would not step on this again
        # But u r using BFS, u might step on some cells because it is near the start
        # But if u continue to walk down this path, u dont have enough modifications
        # But there might be a path that require a detour first and then walk back on this
        # Path, this requires step on stepped cells
        # But if we dont record the stepped cells, it might TLE because u will running in cycles
        # So we need to record stepped cells but can be stepped on again
        # So we record the cells with the modifications made sofar
        q = collections.deque()
        if grid[0][0] == 1:
            k -= 1
        q.append([0, k, 0, 0])
        m, n = len(grid), len(grid[0])
        record = set()
        record.add((0, 0, k))
        while q:
            l = len(q)
            for _ in range(l):
                step, s, x, y = q.popleft()
                if x == m - 1 and y == n - 1:
                    if grid[x][y] == 1 and s == 0:
                        continue
                    return step
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < m and 0 <= j < n:
                        if grid[i][j] == 1:
                            if s >= 1 and (i, j, s - 1) not in record:
                                record.add((i, j, s - 1))
                                q.append([step + 1, s - 1, i, j])
                        else:
                            if (i, j, s) not in record:
                                record.add((i, j, s))
                                q.append([step + 1, s, i, j])
        return -1
