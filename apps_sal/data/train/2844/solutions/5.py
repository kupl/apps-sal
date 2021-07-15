def chessboard(s):
    a,b = map(int,s.split())
    return '\n'.join(('*.'*(b+1))[i&1:(i&1)+b] for i in range(a))
