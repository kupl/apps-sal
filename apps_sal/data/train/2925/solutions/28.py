def multiply(n):
    res = 5 ** len(str(abs(n))) * abs(n)

    return res if n > 0 else -res
