def checkered_board(n):
    return type(n) is int and n >= 2 and '\n'.join([' '.join([['□', '■'][(r + c + n) % 2] for r in range(n)]) for c in range(n)])
