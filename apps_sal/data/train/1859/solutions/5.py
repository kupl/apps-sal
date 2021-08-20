class Solution:

    def validate_sub_matrix(self, matrix, rstart, cstart, size):
        for row in range(size + 1):
            for col in range(size + 1):
                if matrix[rstart + row][cstart + col] == 0:
                    return False
        return True

    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == 0:
                    continue
                s_size = 0
                while row + s_size < num_rows and col + s_size < num_cols and self.validate_sub_matrix(matrix, row, col, s_size):
                    count += 1
                    s_size += 1
        return count
