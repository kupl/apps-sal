class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        height = len(matrix)
        length = len(matrix[0])
        (one_locations, square_submatrices) = self.get_one_locations(matrix)
        current_count = 0
        for size in range(2, min(height, length) + 1):
            if size != 2 and current_count < 4:
                return square_submatrices
            current_count = 0
            for location in one_locations:
                h = location[0]
                l = location[1]
                if h + size - 1 < len(matrix) and l + size - 1 < len(matrix[0]):
                    if self.check_all_ones(matrix, h, l, size):
                        current_count += 1
            square_submatrices += current_count
        return square_submatrices

    def check_all_ones(self, matrix, height, length, square_size):
        for i in range(height, height + square_size):
            for j in range(length, length + square_size):
                if matrix[i][j] != 1:
                    return False
        return True

    def get_one_locations(self, matrix):
        one_locations = set()
        one_count = 0
        for (i, j) in enumerate(matrix):
            for (m, n) in enumerate(matrix[i]):
                if n == 1:
                    one_locations.add((i, m))
                    one_count += 1
        return (one_locations, one_count)
