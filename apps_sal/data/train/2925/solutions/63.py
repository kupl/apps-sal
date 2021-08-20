def multiply(n):
    return n * 5 ** len(list(filter(str.isdigit, str(n))))
