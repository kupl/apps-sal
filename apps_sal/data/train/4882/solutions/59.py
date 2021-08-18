def round_to_next5(n):
    if n % 5 == 0:
        return n
    if n == 0:
        return 0

    return ((n // 5) + 1) * 5
