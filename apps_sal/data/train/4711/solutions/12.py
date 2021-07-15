def zeros(n):
    a = n // 5
    if a >= 5:
        return a + zeros(a)
    else:
        return a
