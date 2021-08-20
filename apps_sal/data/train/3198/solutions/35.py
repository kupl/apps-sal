def check_exam(a, b):
    return max(0, sum(([4, -1, 0][(x != y) + (y == '')] for (x, y) in zip(a, b))))
