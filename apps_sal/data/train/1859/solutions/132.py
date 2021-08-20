class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        squares = {1: set()}
        max_l = min(len(matrix), len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    squares[1].add((i, j))
        for l in range(2, max_l + 1):
            squares[l] = set()
            for s in squares[l - 1]:
                right = (s[0] + 1, s[1])
                down = (s[0], s[1] + 1)
                down_right = (s[0] + 1, s[1] + 1)
                if right in squares[l - 1] and down in squares[l - 1] and (down_right in squares[l - 1]):
                    squares[l].add(s)
        return sum([len(s) for s in squares.values()])
