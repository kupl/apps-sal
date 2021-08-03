from itertools import permutations


def late_clock(digits):
    return max(
        f'{a}{b}:{c}{d}'
        for a, b, c, d in permutations(digits)
        if 0 <= a * 10 + b < 24 and 0 <= c * 10 + d < 60
    )
