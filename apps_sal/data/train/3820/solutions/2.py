def checkered_board(n):
    if not (isinstance(n, int) and n > 1):
        return False
    return '\n'.join(' '.join('□■'[(n + i + j) % 2] for j in range(n)) for i in range(n))
