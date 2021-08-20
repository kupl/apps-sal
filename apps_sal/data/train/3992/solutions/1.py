def is_happy(n):
    while n > 4:
        n = sum((int(d) ** 2 for d in str(n)))
    return n == 1
