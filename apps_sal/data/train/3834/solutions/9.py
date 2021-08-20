def palin(a, b):
    left = str(10 ** ((a - 1) // 2) + (b - 1))
    right = str(left[::-1][a % 2:])
    return int(left + right)
