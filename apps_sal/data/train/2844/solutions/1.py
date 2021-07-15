chessboard = lambda s: '\n'.join(([''.join(['.' if (x + y) % 2 else '*' for x in range(int(s.split()[1]))]) for y in range(int(s.split()[0]))]))
