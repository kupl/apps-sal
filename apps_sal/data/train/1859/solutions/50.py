class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        height, width = len(matrix), len(matrix[0])
        n = 0

        def n_squares(x, y):

            length = 0

            if not matrix[y][x]:
                return 0

            while x + length + 1 <= width and y + length + 1 <= height:

                content = [row[x: x + length + 1] for row in matrix[y: y + length + 1]]
                if not all(i for j in content for i in j):
                    break

                length += 1

            return length

        for x in range(width):
            for y in range(height):
                n += n_squares(x, y)

        return n
