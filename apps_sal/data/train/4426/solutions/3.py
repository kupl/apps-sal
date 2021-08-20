def isMultiple(a, b, n):
    x = round(float('.' + str(a / b + 1e-05).split('.')[-1]), 1)
    x = x * 10 if x < 1 else x
    return x != 0 and x % n == 0
