MOVE = [lambda d, x, y, l: (x, y + d, l), lambda d, x, y, l: (x + d, y, l), lambda d, x, y, l: (x, y - d, l), lambda d, x, y, l: (x - d, y, l)]


def solomons_quest(arr):
    x = y = l = 0
    for a, b, c in arr:
        x, y, l = MOVE[b](c * 2**(l + a), x, y, l + a)
    return [x, y]
