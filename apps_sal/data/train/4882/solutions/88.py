def round_to_next5(n):
    if n % 5 == 0:
        return n
    elif n > 0:
        return int(n / 5 + 1) * 5
    elif n < 0:
        return int(n / 5) * 5
