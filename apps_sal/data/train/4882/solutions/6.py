def round_to_next5(n):
    return n if n % 5 == 0 else round_to_next5(n + 1)
