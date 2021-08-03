def max_multiple(a, b):
    while b % a != 0:
        b -= 1
    return b
