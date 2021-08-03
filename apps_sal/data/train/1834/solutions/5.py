class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        '''
        top priority would be the first column should be all 1s
        so toggle each row to make sure the first cell is 1
        and examine each column from left to right
        toggle if needed to make sure sum of each column is bigger than otherwise
        '''

        def toggle_row(row):
            for j in range(len(A[0])):
                if A[row][j] == 1:
                    A[row][j] = 0
                else:
                    A[row][j] = 1

        def toggle_col(col):
            for i in range(len(A)):
                if A[i][col] == 1:
                    A[i][col] = 0
                else:
                    A[i][col] = 1

        for i in range(len(A)):
            if A[i][0] == 0:
                toggle_row(i)

        for j in range(1, len(A[0])):
            # get col sum
            col_sum = 0
            for i in range(len(A)):
                col_sum += A[i][j]
            if col_sum < len(A) / 2:
                toggle_col(j)

        # convert into binary and calculate result
        res = 0
        for row in A:
            row_s = ''
            for i in row:
                row_s += str(i)
            decimal = int(row_s, 2)
            res += decimal
        return res
