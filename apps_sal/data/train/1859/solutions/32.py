class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                search_space_increase = 0
                while row + search_space_increase < len(matrix) and col + search_space_increase < len(matrix[0]):
                    end_row = row + search_space_increase
                    end_col = col + search_space_increase
                    is_valid = True
                    for start_row in range(row, end_row + 1):
                        for start_col in range(col, end_col + 1):
                            if matrix[start_row][start_col] != 1:
                                is_valid = False
                                break
                        if not is_valid:
                            break
                    if not is_valid:
                        break
                    result += 1
                    search_space_increase += 1
        return result
