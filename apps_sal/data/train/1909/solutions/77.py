class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        sum_row = []
        sum_col = []
        for i in range(m):
            sum_row.append([0]*n)
            sum_col.append([0]*n)
        for i in range(m):
            # print(i)
            sum_row[i][0] = grid[i][0]
            # print(sum_row[i][0], grid[i][0])
            # print(sum_row[0], sum_row[1], sum_row[2])
            for j in range(1, n):
                # print(i, j)
                sum_row[i][j] = sum_row[i][j-1] + grid[i][j]
                # print(sum_row)
        # print(sum_row, 'end') 
        for j in range(n):
            sum_col[0][j] = grid[0][j]
            for i in range(1, m):
                sum_col[i][j] = sum_col[i-1][j] + grid[i][j]
        # print(sum_col, 'end')
        # scan all possible squares
        num_ele = 0
        for i in range(m):
            for j in range(n):
                l = min(i, j)
                # print(i, j, l)
                for k in range(l+1):
                    slen = l-k
                    length = slen + 1
                    # print(i, j, l, k, slen, length)
                    if ((sum_row[i-slen][j] - sum_row[i-slen][j-slen] + grid[i-slen][j-slen]) == length
                    and (sum_row[i][j] - sum_row[i][j-slen] + grid[i][j-slen]) == length
                    and (sum_col[i][j-slen] - sum_col[i-slen][j-slen] + grid[i-slen][j-slen]) == length
                    and (sum_col[i][j] - sum_col[i-slen][j] + grid[i-slen][j]) == length):
                        if length*length > num_ele:
                            num_ele = length*length
                        break
        return num_ele
                    

