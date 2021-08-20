def zeros(n):
    if n == 0:
        return 0
    value = 0
    i = 1
    while True:
        if n > 5 ** i:
            value += n // 5 ** i
        else:
            return value
        i += 1
