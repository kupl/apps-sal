def zeros(n):
    return 0 if not n else n // 5 + zeros(n // 5)
