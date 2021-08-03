def multiply(n):
    n = str(n)
    if int(n) >= 0:
        l = len(n)
    else:
        l = len(n) - 1
    n = int(n)
    return n * (5**l)
