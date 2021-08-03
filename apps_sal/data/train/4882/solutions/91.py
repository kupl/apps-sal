def round_to_next5(n):
    if n % 5 != 0:
        return (n // 5 + 1) * 5
    elif n % 5 == 0:
        return n
    else:
        return 0
