def chessboard(s):
    r,c=map(int,s.split())
    return "\n".join("".join("*."[j%2!=i%2] for j in range(c)) for i in range(r))
