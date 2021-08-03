def digits(n):
    return 1 if n < 10 else 1 + digits(n // 10)
    pass
