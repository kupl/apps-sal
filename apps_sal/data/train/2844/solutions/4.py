def chessboard(s):
    (rows, cols) = map(int, s.split())
    if rows and cols:
        return '\n'.join((''.join(('*.'[(i + j) % 2] for i in range(cols))) for j in range(rows)))
    return ''
