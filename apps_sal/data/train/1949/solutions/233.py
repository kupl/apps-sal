class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        path_indices = [0, 1, 2, 3]

        def value(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            return grid[i][j]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid[i][j] == 0:
                return 0

            visited.add((i, j))
            golds = [dfs(i + i_, j + j_) for i_, j_ in path]
            idx = max(path_indices, key=lambda x: golds[x])

            gold = grid[i][j] + golds[idx]
            visited.remove((i, j))

            return gold

        visited = set()
        max_gold = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    gold = dfs(i, j)
                    if gold > max_gold:
                        max_gold = gold

        return max_gold
