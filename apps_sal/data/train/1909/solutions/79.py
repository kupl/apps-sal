class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        row = [0] * len(grid[0])
        dph = []
        dpv = []
        for i in range(len(grid)):
            dph.append([0] * len(grid[0]))
            dpv.append([0] * len(grid[0]))

        for i in range(len(grid)):
            if grid[i][0] != 0:
                dph[i][0] = 1
            else:
                dph[i][0] = 0

            for j in range(1, len(grid[0])):
                if grid[i][j] != 0:
                    print((i, j))
                    dph[i][j] = dph[i][j - 1] + 1

                else:

                    dph[i][j] = 0

        for j in range(len(grid[0])):
            if grid[0][j] != 0:
                dpv[0][j] = 1
            else:
                dpv[0][j] = 0

            for i in range(1, len(grid)):
                if grid[i][j] != 0:
                    dpv[i][j] = dpv[i - 1][j] + 1

                else:
                    dpv[i][j] = 0

        print(dpv)
        print(dph)

        maxl = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    startl = min(dpv[i][j], dph[i][j])
                    if startl > maxl:

                        for k in range(startl, maxl, -1):
                            left = j - k + 1
                            top = i - k + 1
                            if dpv[i][left] >= k and dph[top][j] >= k:
                                maxl = k
                                break
        return maxl * maxl
