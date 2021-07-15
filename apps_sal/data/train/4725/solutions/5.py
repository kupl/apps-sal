def reverse(n, r=0):
    return reverse(n // 10, r * 10 + n % 10) if n else r
