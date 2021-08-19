hops = [[-1, 0], [1, 0], [0, 1], [0, -1]]


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        g = 0
        path = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                temp = self.goldHelper(grid, r, c, path)
                # print(temp, r, c)
                g = max(g, temp)
        return g

    def goldHelper(self, grid: List[List[int]], r, c, path):
        if (r, c) in path:
            return 0

        if r < 0 or r >= len(grid):
            return 0

        if c < 0 or c >= len(grid[0]):
            return 0

        if grid[r][c] == 0:
            return 0

        path.add((r, c))
        curr = 0

        for v, a in hops:
            curr = max(curr, self.goldHelper(grid, r + v, c + a, path))

        path.remove((r, c))

        return curr + grid[r][c]
