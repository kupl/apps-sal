class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
            # If matrix is empty: return 0
        if not matrix:
            return 0

        # For every '1' encountered, increment count by 1

        # Count the number of '1s' for each row
        #    Unsure yet: record start, and stop index
        
        count = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        count += 1
                    else:
                        cell = min(matrix[row-1][col], matrix[row-1][col-1], matrix[row][col-1]) + matrix[row][col]
                        count += cell
                        matrix[row][col] = cell
        return count
