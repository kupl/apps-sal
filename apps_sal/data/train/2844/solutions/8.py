def chessboard(s):
    (m, n) = map(int, s.split())
    return '\n'.join((('*.' * n)[i % 2:n + i % 2] for i in range(m)))
