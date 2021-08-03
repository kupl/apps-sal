def round_to_next5(n):
    return int(n / 5 + (n % 5 != 0)) * 5 if n >= 0 else int(n / 5) * 5
