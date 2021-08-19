def checkered_board(n):
    l = ['□', '■']
    return False if type(n) != int or n < 2 else '\n'.join((' '.join((l[(i + j + n) % 2] for i in range(n))) for j in range(n)))
