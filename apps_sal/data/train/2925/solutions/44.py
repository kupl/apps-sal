def multiply(n):
    print(n)
    return 5 ** len(str(n)) * n if n > 0 else 5 ** (len(str(n)) - 1) * n
