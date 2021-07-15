def last_digit(n1, n2):
    if n2 == 0:
        return 1
    n1 %= 10
    if n1 in [0, 1, 5, 6]:
        return n1
    if n1 == 2:
        return [6, 2, 4, 8][n2%4]
    if n1 == 3:
        return [1, 3, 9, 7][n2%4]
    if n1 == 4:
        return [6, 4][n2%2]
    if n1 == 7:
        return [1, 7, 9, 3][n2%4]
    if n1 == 8:
        return [6, 8, 4, 2][n2%4]
    return [1, 9][n2%2]

