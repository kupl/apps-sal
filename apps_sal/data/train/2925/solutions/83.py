def multiply(n):
    if n < 0:
        n = -n
        s = len(str(n))
        return 5 ** s * n * -1
    else:
        s = len(str(n))
        return 5 ** s * n
