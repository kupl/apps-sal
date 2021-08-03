basics = [0, 4, 10, 20, 35, 56, 83, 116, 155, 198, 244, 292]


def solve(n):
    return basics[n] if n < 12 else 49 * n - 247
