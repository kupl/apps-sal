def round_to_next5(n):
    if n % 10 > 5:
        return n - (n % 10) + 10
    elif n % 10 == 5 or n % 10 == 0:
        return n
    else:
        return n + (5 - (n % 10))
