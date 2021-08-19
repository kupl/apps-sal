class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        (m, n) = (len(grid), len(grid[0]))

        def dfs(i, j, visited, res):
            nonlocal result, best_path
            if res > result:
                best_path = visited
            ret = res
            for (a, b) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                (ci, cj) = (a + i, b + j)
                if 0 <= ci < m and 0 <= cj < n and ((ci, cj) not in visited) and (grid[ci][cj] != 0):
                    ret = max(ret, dfs(ci, cj, visited | set([(ci, cj)]), res + grid[ci][cj]))
            return ret
        result = 0
        best_path = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in best_path:
                    result = max(result, dfs(i, j, set([(i, j)]), grid[i][j]))
        return result
