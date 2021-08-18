def round_to_next5(n):
    return 5 * (n // 5 + int(bool(n % 5)))
