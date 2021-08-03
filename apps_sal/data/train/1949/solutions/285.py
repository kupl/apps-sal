class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def getGold(i, j, s, money):
            nonlocal mx
            for c1, c2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (c1, c2) not in s and 0 <= c1 < len(grid) and 0 <= c2 < len(grid[0]) and grid[c1][c2] != 0:
                    s.add((c1, c2))
                    getGold(c1, c2, s, money + grid[c1][c2])
                    s.remove((c1, c2))
            mx = max(mx, money)

        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s = set()
                if grid[i][j] != 0:
                    s.add((i, j))
                    getGold(i, j, s, grid[i][j])
        return mx
