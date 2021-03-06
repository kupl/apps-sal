class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        import copy

        def grow_sqaure(x, y):
            oriX = copy.copy(x)
            oriY = copy.copy(y)
            still_square = False
            count = 0
            if matrix[x][y] == 1:
                still_square = True
            while x < len(matrix) and y < len(matrix[0]) and still_square:
                for i in range(oriX, x + 1):
                    for j in range(oriY, y + 1):
                        if matrix[i][j] != 1:
                            still_square = False
                            return count
                count += 1
                x += 1
                y += 1
            return count
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count += grow_sqaure(i, j)
        return count
