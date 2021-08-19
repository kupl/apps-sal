def multiply(n):
    if n == 0:
        return 0
    elif n > 0:
        exp = len(str(n))
        return n * 5 ** exp
    else:
        exp = len(str(-n))
        return n * 5 ** exp
