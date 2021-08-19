def number_increasing(n):
    if n == 2 or n == 4:
        return False
    if n % 5 == 1:
        return True
    for v in [3 ** i for i in range(1, 11)]:
        if (v - n) % 5 == 0:
            return True
    return False
