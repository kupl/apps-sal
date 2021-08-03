def round_to_next5(n):
    return (n // 5 + (1 if n % 5 != 0 else 0)) * 5
