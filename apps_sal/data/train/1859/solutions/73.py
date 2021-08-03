class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        num_squares = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                num_squares += squaresAt(x, y, matrix)
        return num_squares


def squaresAt(x: int, y: int, matrix: List[List[int]]) -> int:

    size = 0

    while True:

        if y + size >= len(matrix):
            break
        if x + size >= len(matrix[0]):
            break

        good_row = checkRow(x, x + size, y + size, matrix)
        good_col = checkCol(x + size, y, y + size, matrix)

        if good_row and good_col:
            size += 1
        else:
            break

    return size


def checkRow(x1: int, x2: int, y: int, matrix: List[List[int]]) -> bool:
    for x in range(x1, x2 + 1):
        if matrix[y][x] == 0:
            return False
    return True


def checkCol(x: int, y1: int, y2: int, matrix: List[List[int]]) -> bool:

    for y in range(y1, y2 + 1):
        if matrix[y][x] == 0:
            return False
    return True
