class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # For every possible size (min(height, length))
        # For every location of a 1
        # Check if all 1's (if the remaining array sizes are valid i.e i + size < len(matrix) and j + size < len(matrix[0]))

        # On the next size check, only continue if the previous step found at least 4.
        # Error Checking
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # General Case
        height = len(matrix)
        length = len(matrix[0])
        one_locations, square_submatrices = self.get_one_locations(matrix)

        current_count = 0
        for size in range(2, min(height, length) + 1):
            if size != 2 and current_count < 4:
                return square_submatrices

            # Reset the count
            current_count = 0

            for location in one_locations:
                # Check if it can even be valid before searching
                h = location[0]
                l = location[1]

                if (h + size - 1) < len(matrix) and (l + size - 1) < len(matrix[0]):
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

        for i, j in enumerate(matrix):
            for m, n in enumerate(matrix[i]):
                if n == 1:
                    one_locations.add((i, m))
                    one_count += 1

        return one_locations, one_count
