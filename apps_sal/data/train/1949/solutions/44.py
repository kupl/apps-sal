class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        # 这题的space可以不用seen而用mark grid为0表示已经被visited
        # 但是并没有优化space，因为stack里面还是要存那么多tmp！！！
        # space 是longest path length/dfs depth，bounded by n*n
        # time是 k*4*3^(k-1) 因为第一个可能4个方向，后面每个最多3个方向
        maxGold = 0
        #seen = set()
        m, n = len(grid), len(grid[0])

        def dfs(i, j):  # position, cannot use cache.
            res = 0
            if grid[i][j] == 0:
                return 0
            #seen.add((i, j))
            tmp = grid[i][j]
            grid[i][j] = 0
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n:
                    # if (x, y) in seen: continue
                    res = max(res, dfs(x, y))

            #seen.discard((i, j))
            grid[i][j] = tmp
            return res + grid[i][j]

        for i in range(m):
            for j in range(n):
                maxGold = max(maxGold, dfs(i, j))

        return maxGold
