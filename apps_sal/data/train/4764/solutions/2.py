def rotate_clockwise(m):
    return list(map(''.join, zip(*m[::-1])))
