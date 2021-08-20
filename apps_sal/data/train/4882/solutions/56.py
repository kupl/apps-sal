def round_to_next5(n):
    return n // 5 * 5 + (abs(n) % 5 > 0) * 5
