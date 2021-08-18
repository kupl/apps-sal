class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        row = len(mat)
        col = len(mat[0])

        answer = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(1, col):
                mat[i][j] = mat[i][j - 1] + mat[i][j]
        print(mat)

        for i in range(row):
            for j in range(col):
                answer[i][j] = self.new_matrix(mat, i, j, K, row, col)
        return answer

    def new_matrix(self, mat, i, j, k, row, col):
        ans = 0
        new_row_low = i - k
        new_row_high = i + k
        new_col_low = j - k
        new_col_high = j + k

        while(new_row_low < 0):
            new_row_low += 1
        while(new_row_high > row - 1):
            new_row_high -= 1
        while(new_col_low < 0):
            new_col_low += 1
        while(new_col_high > col - 1):
            new_col_high -= 1

        for a in range(new_row_low, new_row_high + 1):

            ans += mat[a][new_col_high]

            if(new_col_low - 1 >= 0):

                ans -= mat[a][new_col_low - 1]

        return ans
