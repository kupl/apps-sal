def zeros(n):
    res = 0
    i = 5
    while i <= n:
        res += n // i
        i *= 5
    return res
