class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        max_path = 0

        def index_gen(index):
            (i, j) = index
            if i > 0 and grid[i - 1][j] > 0:
                yield (i - 1, j)
            if i < height - 1 and grid[i + 1][j] > 0:
                yield (i + 1, j)
            if j > 0 and grid[i][j - 1] > 0:
                yield (i, j - 1)
            if j < width - 1 and grid[i][j + 1] > 0:
                yield (i, j + 1)

        def is_viable(index):
            non_zero = 0
            neighbors = [grid[a][b] for (a, b) in index_gen(index)]
            for x in neighbors:
                if x != 0:
                    non_zero += 1
            return non_zero < 2

        def dfs(index, count):
            nonlocal max_path
            count += grid[index[0]][index[1]]
            max_path = max(max_path, count)
            grid[index[0]][index[1]] *= -1
            for direction in index_gen(index):
                dfs(direction, count)
            grid[index[0]][index[1]] *= -1
        for i in range(height):
            for j in range(width):
                if grid[i][j] != 0 and is_viable((i, j)):
                    dfs((i, j), 0)
        return max_path if max_path > 0 else sum((sum(row) for row in grid))
        '\n        if len(grid) == 0 or len(grid[0]) == 0:\n            return 0\n        \n        def collectGold(r, c, goldSoFar):\n            \n            pts = [[0,1],[1,0],[-1,0],[0,-1]]\n            \n            maxGold = goldSoFar\n            \n            for p in pts:\n                nR = p[0] + r\n                nC = p[1] + c\n                \n                if 0 <= nR < len(grid) and 0<= nC < len(grid[0]) and grid[nR][nC] != 0:\n                    v = grid[nR][nC]\n                    grid[nR][nC] = 0\n                    gold = collectGold(nR, nC, goldSoFar + v)\n                    maxGold = max(gold, maxGold)\n                    grid[nR][nC] = v\n                    \n            return maxGold\n        \n        maxGold = 0\n        for i in range(len(grid)):\n            for j in range(len(grid[0])):\n                if grid[i][j] != 0:\n                    v = grid[i][j]\n                    grid[i][j] = 0\n                    gold = collectGold(i, j, v)\n                    maxGold = max(maxGold, gold)\n                    grid[i][j] = v\n        return maxGold\n        '
