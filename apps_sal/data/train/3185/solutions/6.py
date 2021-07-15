def rotate_against_clockwise(m, n):
    for _ in range(n % 4): m = [[r[i] for r in m] for i in range(len(m))][::-1]
    return m
