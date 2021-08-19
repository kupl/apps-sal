class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # [0,1,1,1]
        # [1,1,2,2]
        # [0,1,2,3] 15

        # leave the border as-is
        # using same matrix: O(1) space, O(nm) time
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 1:  # if 0: ignore
                    ul = matrix[row - 1][col - 1]
                    u = matrix[row - 1][col]
                    l = matrix[row][col - 1]
                    val = min(ul, u, l) + 1
                    matrix[row][col] = val
        # print(matrix)
        total = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                total += matrix[row][col]
        return total
