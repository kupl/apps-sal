class Solution:
    max_gold = 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (nRow, nCol) = (len(grid), len(grid[0]))
        self.max_gold = max([x for r in grid for x in r])
        path = []

        def helper(kr, kc):
            up = kr == 0 or grid[kr - 1][kc] == 0
            down = kr == nRow - 1 or grid[kr + 1][kc] == 0
            left = kc == 0 or grid[kr][kc - 1] == 0
            right = kc == nCol - 1 or grid[kr][kc + 1] == 0
            if up and down and left and right:
                self.max_gold = max(self.max_gold, sum(path) + grid[kr][kc])
            else:
                path.append(grid[kr][kc])
                grid[kr][kc] = 0
                if not up:
                    helper(kr - 1, kc)
                if not down:
                    helper(kr + 1, kc)
                if not left:
                    helper(kr, kc - 1)
                if not right:
                    helper(kr, kc + 1)
                grid[kr][kc] = path.pop()
        for kr in range(nRow):
            for kc in range(nCol):
                if grid[kr][kc]:
                    helper(kr, kc)
        return self.max_gold
