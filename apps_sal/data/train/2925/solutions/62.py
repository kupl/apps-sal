def multiply(n):
    a = []
    if n < 0:
        a2 = str(n)
        a3 = len(a2)
        a4 = a3 - 1
    if n > 0:
        d = str(n)
        c = len(d)
    if n == 0:
        return 0
    elif n < 0:
        return 5 ** a4 * n
    elif n > 0:
        return 5 ** c * n
