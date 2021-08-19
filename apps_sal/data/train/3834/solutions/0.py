def palin(length, pos):
    left = str(10 ** ((length - 1) // 2) + (pos - 1))
    right = left[::-1][length % 2:]
    return int(left + right)
