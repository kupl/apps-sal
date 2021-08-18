class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def is_valid_square(start_row, end_row, start_col, end_col, matrix):

            return not any(matrix[row][col] == 0 for row in range(start_row, end_row + 1) for col in range(start_col, end_col + 1))

        result = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                search_space_increase = 0
                while row + search_space_increase < len(matrix) and col + search_space_increase < len(matrix[0]):
                    if not is_valid_square(row, row + search_space_increase, col, col + search_space_increase, matrix):
                        break
                    result += 1
                    search_space_increase += 1

        return result
