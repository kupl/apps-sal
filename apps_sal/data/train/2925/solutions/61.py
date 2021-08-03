def multiply(n):
    power = len(str(n))
    if n > 0:
        return n * (5**power)
    if n < 0:
        power = len(str(n)) - 1
        return n * (5**power)
    else:
        return 0
