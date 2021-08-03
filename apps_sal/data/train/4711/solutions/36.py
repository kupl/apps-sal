def zeros(n):
    return 0 if n < 5 else n // 5 + zeros(n // 5)
