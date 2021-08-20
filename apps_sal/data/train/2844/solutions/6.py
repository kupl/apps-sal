def chessboard(s):
    (row, column) = [int(num) for num in s.split()]
    return '\n'.join((''.join(('*.'[(i + j) % 2] for j in range(column))) for i in range(row)))
