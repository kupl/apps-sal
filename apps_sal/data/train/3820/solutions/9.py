def checkered_board(n):
    if isinstance(n, int) and n > 1:
        return '\n'.join((' '.join(('□' if ((i % 2 == j % 2) ^ n) % 2 else '■' for j in range(n))) for i in range(n)))
    else:
        return False
