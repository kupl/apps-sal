def round_to_next5(n):
    r = n % 5
    return 5 + (n - r) if r != 0 else n
