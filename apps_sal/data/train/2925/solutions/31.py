def multiply(n):
    if '-' in str(n):
        i = len(str(n)) - 1
    else:
        i = len(str(n))
    return n * 5 ** i
