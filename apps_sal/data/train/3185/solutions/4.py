def rotate_against_clockwise(a, n):
    return rotate_against_clockwise(list(zip(*a))[::-1], n - 1) if n % 4 else list(map(list, a))
