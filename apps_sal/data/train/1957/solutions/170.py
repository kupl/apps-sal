class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] == 1 and k == 0:
            return -1

        m, n = len(grid), len(grid[0])
        if grid[0][0]:
            k -= 1
        qe = collections.deque([(0, 0, 0, k)])

        visited = set()
        visited.add((0, 0, k))

        dr = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while qe:
            i, j, step, k = qe.popleft()
            if i == m - 1 and j == n - 1:
                return step

            for x, y in dr:
                i1, j1 = i + x, j + y
                if i1 < 0 or i1 >= m or j1 < 0 or j1 >= n:
                    continue
                if grid[i1][j1] == 1 and k == 0:
                    continue
                if grid[i1][j1] == 1 and k >= 1 and (i1, j1, k - 1) not in visited:
                    visited.add((i1, j1, k - 1))
                    qe.append((i1, j1, step + 1, k - 1))
                if grid[i1][j1] == 0 and k >= 0 and (i1, j1, k) not in visited:
                    if i1 == m - 1 and j1 == n - 1:
                        return step + 1
                    visited.add((i1, j1, k))
                    qe.append((i1, j1, step + 1, k))

        return -1
