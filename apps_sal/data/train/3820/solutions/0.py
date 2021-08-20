def checkered_board(n):
    return isinstance(n, int) and n > 1 and '\n'.join((' '.join(('■' if (x + y) % 2 ^ n % 2 else '□' for y in range(n))) for x in range(n)))
