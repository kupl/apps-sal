def chessboard(s):
    (w, h) = map(int, s.split())
    return '\n'.join((''.join(('*.'[(i + j) % 2] for i in range(h))) for j in range(w)))
