def multiply(n):
    if n < 0:
        return n * (5 ** len(str(n * -1)))

    return n * (5 ** len(str(n)))
