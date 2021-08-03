def is_divisible(n, x, y):
    correct = True
    if n / x != n // x:
        correct = False
    elif n / y != n // y:
        correct = False
    return correct
