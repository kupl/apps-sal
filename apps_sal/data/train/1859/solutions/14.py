class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                temp = matrix[row][col]
                ans += matrix[row][col]
                if(row > 0):
                    matrix[row][col] += matrix[row-1][col]
                if(col > 0):
                    matrix[row][col] += matrix[row][col-1]
                if(row > 0 and col > 0):
                    matrix[row][col] -= matrix[row-1][col-1]
                if not temp: continue
                side = 1
                while(row-side >= 0 and col-side >= 0):
                    s = matrix[row][col]
                    if(col-side > 0):
                        s -= matrix[row][col-side-1]
                    if(row-side > 0):
                        s -= matrix[row-side-1][col]
                    if(col-side > 0 and row-side > 0):
                        s += matrix[row-side-1][col-side-1]
                    if(s == (side+1)*(side+1)):
                        ans += 1
                    else:
                        break
                    side += 1
        return ans
