class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        dp = [[None] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = (1, 1) if grid[0][0] == 1 else (0, 0)

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if r == 0 and c == 0:
                    continue
                # handle first row
                elif r == 0:
                    if grid[0][c] == 1:
                        newR = 1
                        newC = 1 + dp[0][c - 1][1]
                        dp[r][c] = (newR, newC)
                    else:
                        dp[r][c] = (0, 0)

                elif c == 0:
                    if grid[r][0] == 1:
                        newR = 1 + dp[r - 1][0][0]
                        newC = 1
                        dp[r][c] = (newR, newC)
                    else:
                        dp[r][c] = (0, 0)
                else:
                    if grid[r][c] == 1:
                        newR = 1 + dp[r - 1][c][0]
                        newC = 1 + dp[r][c - 1][1]
                        dp[r][c] = (newR, newC)
                    else:
                        dp[r][c] = (0, 0)

        # print(dp)
        maxGrid = 0
        # now lets iterate from bottom right to upper left
        for r in range(len(grid) - 1, -1, -1):
            for c in range(len(grid[0]) - 1, -1, -1):

                minSpan = min(dp[r][c][0], dp[r][c][1])
                if minSpan == 0:
                    continue
                # print('r',r,'c',c,'minSpan',minSpan)
                # we need to loop through min span
                for span in range(minSpan, -1, -1):
                    # check left dp span and see if its row == minSpan
                    cSpanLeft = c - span + 1
                    rSpanUp = r - span + 1
                    # print(r,c,cSpanLeft,rSpanUp)
                    # print('dp[r][cSpanLeft][0]',dp[r][cSpanLeft][0],'dp[rSpanUp][c][1]',dp[rSpanUp][c][1] )
                    if dp[r][cSpanLeft][0] >= span and dp[rSpanUp][c][1] >= span:
                        # print('maxis', minSpan)
                        maxGrid = max(maxGrid, span**2)
                        break

        return maxGrid
