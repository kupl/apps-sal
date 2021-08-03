from numpy import prod


def per(n):
    if n < 10:
        return []
    arr = []
    while n > 9:
        n = prod([int(i) for i in str(n)])
        arr.append(n)
    return arr
