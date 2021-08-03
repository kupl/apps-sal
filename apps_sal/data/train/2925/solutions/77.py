def multiply(n):
    power = len(str(n))

    if n < 0:
        power -= 1

    return n * 5 ** power
