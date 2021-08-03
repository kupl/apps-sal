def fusc(n):
    return n if n < 2 else fusc(n // 2) + (n % 2 and fusc(n // 2 + 1))
