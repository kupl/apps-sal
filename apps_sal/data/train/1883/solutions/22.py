class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        self.ans, self.count = 0, 0

        def go(cur, seen):
            i, j = cur
            if grid[i][j] == 2:
                if len(seen) == self.count:
                    self.ans += 1
                else:
                    return

            for r, c, in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c] != -1:
                    seen.add((r, c))
                    go((r, c), seen)
                    seen.remove((r, c))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in [0, 1, 2]:
                    self.count += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    go((i, j), {(i, j)})
                    return self.ans

        return ans
