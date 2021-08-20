class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(i: int, j: int, sum_so_far: int, seen: set) -> int:
            if i < 0 or i >= m or j < 0 or (j >= n) or (not grid[i][j]) or ((i, j) in seen):
                return sum_so_far
            seen.add((i, j))
            sum_so_far += grid[i][j]
            mx = 0
            for (x, y) in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                mx = max(dfs(x, y, sum_so_far, seen), mx)
            seen.discard((i, j))
            return mx
        (m, n) = (len(grid), len(grid[0]))
        all_gold_path = []
        for row in range(m):
            for col in range(n):
                all_gold_path.append(dfs(row, col, 0, set()))
        return max(all_gold_path)
