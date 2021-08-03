def multiply(n):
    for x in range(len(str(n))):
        n *= 5
    return n if n > 0 else n / 5
