def multiply(n):
    count = len(str(n))
    if n >= 0:
        return n * 5 ** count
    else:
        return n * 5 ** (count - 1)
