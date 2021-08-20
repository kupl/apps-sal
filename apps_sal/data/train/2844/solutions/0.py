def chessboard(s):
    (N, M) = map(int, s.split())
    row = '.*' * M
    return '\n'.join([row[:M] if i & 1 else row[1:M + 1] for i in range(N)])
