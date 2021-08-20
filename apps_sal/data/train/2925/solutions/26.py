def multiply(n):
    return n * 5 ** len(str(n if n > 0 else n * -1))
