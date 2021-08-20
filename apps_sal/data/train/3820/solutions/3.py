def checkered_board(n):
    if type(n) != int or n < 2:
        return False
    s1 = ' '.join(('■□'[i & 1] for i in range(n)))
    s2 = ' '.join(('□■'[i & 1] for i in range(n)))
    lines = [s1, s2] if n & 1 else [s2, s1]
    return '\n'.join((lines[i & 1] for i in range(n)))
