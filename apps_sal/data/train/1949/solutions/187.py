class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        results = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                tmp = grid[i][j]
                grid[i][j] = '*'
                self.helper([tmp], i, j, grid, results)
                grid[i][j] = tmp
        maxV = -sys.maxsize
        for i in results:
            if sum(i) > maxV:
                maxV = sum(i)
        return maxV

    def helper(self, sub, ii, jj, grid, results):
        if sub[-1] == 0:
            results.append(sub.copy())
            return

        ll = [[ii - 1, jj], [ii + 1, jj], [ii, jj - 1], [ii, jj + 1]]

        for l in ll:

            if l[0] < 0 or l[0] > len(grid) - 1:
                continue
            if l[1] < 0 or l[1] > len(grid[0]) - 1:
                continue
            if grid[l[0]][l[1]] == '*':
                continue

            sub.append(grid[l[0]][l[1]])
            tmp = grid[l[0]][l[1]]
            grid[l[0]][l[1]] = '*'
            self.helper(sub, l[0], l[1], grid, results)
            grid[l[0]][l[1]] = tmp
            sub.pop()
