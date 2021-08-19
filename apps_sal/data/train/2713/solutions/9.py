STARTERS = (0, 4, 10, 20, 35, 56, 83, 116, 155, 198, 244)


def solve(n):
    return STARTERS[n] if n < 11 else 292 + 49 * (n - 11)
