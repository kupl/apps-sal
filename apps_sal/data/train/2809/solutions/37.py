def digitize(n):
    n = str(n)
    digits = [int(s) for s in n]
    return digits[::-1]
