def factorial(n):
    return -1 if n < 0 else 1 if n == 0 else n * factorial(n - 1)

def am_i_wilson(n):
    if n < 2:
        return False
    elif n in [5, 13, 563]:
        return True
    else:
        return False
    #f = (factorial(n - 1) + 1) / (n * n)
    return str(n)
