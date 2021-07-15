def multiply(n):
    return n * 5 ** len(str(n)) if str(n)[0] != "-" else n * 5 ** (len(str(n)) - 1)
