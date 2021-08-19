def branch(n):
    if n == 1:
        return 0
    i = 1
    while True:
        if n <= (2 * i - 1) ** 2:
            break
        i += 1
    return int((n - (2 * i - 3) ** 2 - 1) / (2 * i - 2))
