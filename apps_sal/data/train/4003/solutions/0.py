def possible_positions(p):
    r, c = ord(p[0])-96, int(p[1])
    moves = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
    return [''.join((chr(r+i+96), str(c+j))) for i, j in moves if 1 <= r+i <= 8 and 1 <= c+j <= 8]
