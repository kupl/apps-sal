class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        path_store = deque([((0, 0), 0, k)])
        seen = {}
        while path_store:
            temp = path_store.pop()
            (s, t) = temp[0]
            if s == m - 1 and t == n - 1:
                return temp[1]
            for (i, j) in [(s + 1, t), (s, t + 1), (s - 1, t), (s, t - 1)]:
                if i < 0 or i >= m or j < 0 or (j >= n) or (k == 0 and grid[i][j] == 1) or (seen.get((i, j), -1) >= temp[2] - (grid[i][j] == 1)):
                    continue
                seen[i, j] = temp[2] - (grid[i][j] == 1)
                path_store.appendleft(((i, j), temp[1] + 1, seen[i, j]))
        return -1
