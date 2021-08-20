class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        columns = len(mat[0])
        sum_ = 0
        for (r, c1, c2) in zip(list(range(rows)), list(range(columns)), list(range(columns - 1, -1, -1))):
            sum_ += mat[r][c1]
            if c1 != c2:
                sum_ += mat[r][c2]
        return sum_
