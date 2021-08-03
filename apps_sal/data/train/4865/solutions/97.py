def multiply(n, m, acc=0):
    if m <= 0:
        return acc
    else:
        return multiply(n, m - 1, acc + n)
