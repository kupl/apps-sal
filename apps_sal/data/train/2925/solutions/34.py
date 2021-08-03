def multiply(n):
    if n < 0:
        x = str(n).replace('-', '')
        y = len(x)
        return n * (5**y)
    else:
        return n * (5**len(str(n)))
