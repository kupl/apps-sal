def round_to_next5(n):
    return n if n % 10 == 0 else n + (-n % 5)
