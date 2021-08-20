class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        iMax = len(grid)
        jMax = len(grid[0])
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        numOfGold = 0
        goldNumDict = {}
        for i in range(iMax):
            for j in range(jMax):
                if grid[i][j] != 0:
                    goldNumDict[i, j] = numOfGold
                    numOfGold += 1
        dp = defaultdict(int)

        def findGold(mNow, i0, j0, goldNow):
            subAns = goldNow
            for k in range(4):
                i1 = i0 + di[k]
                j1 = j0 + dj[k]
                if i1 < 0 or j1 < 0 or i1 == iMax or (j1 == jMax) or (grid[i1][j1] == 0) or mNow & 1 << goldNumDict[i1, j1]:
                    continue
                subAns = max(subAns, findGold(mNow | 1 << goldNumDict[i1, j1], i1, j1, goldNow + grid[i1][j1]))
            dp[mNow] = max(subAns, dp[mNow])
            return subAns
        ans = 0
        for i in range(iMax):
            for j in range(jMax):
                if grid[i][j] != 0:
                    ans = max(ans, findGold(1 << goldNumDict[i, j], i, j, grid[i][j]))
        return ans
