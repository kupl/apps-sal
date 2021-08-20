def multiply(n):
    n = str(n)
    if int(n) < 0:
        return int(n) * 5 ** (len(n) - 1)
    else:
        return int(n) * 5 ** len(n)
