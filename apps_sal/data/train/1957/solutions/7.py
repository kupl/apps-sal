class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n, visited) = (len(grid), len(grid[0]), set())
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = collections.deque()
        q.append((0, 0, k))
        visited.add((0, 0, k))
        (res, cnt, total) = (0, 0, 1)
        while q:
            (i, j, r) = q.popleft()
            cnt += 1
            if i == m - 1 and j == n - 1:
                return res
            for d in ds:
                (ni, nj) = (i + d[0], j + d[1])
                if ni >= 0 and ni < m and (nj >= 0) and (nj < n) and ((ni, nj, r) not in visited):
                    if grid[ni][nj] == 0 and (ni, nj, r) not in visited:
                        visited.add((ni, nj, r))
                        q.append((ni, nj, r))
                    elif r > 0 and (ni, nj, r - 1) not in visited:
                        visited.add((ni, nj, r - 1))
                        q.append((ni, nj, r - 1))
            if cnt == total:
                (cnt, total) = (0, len(q))
                res += 1
        return -1
