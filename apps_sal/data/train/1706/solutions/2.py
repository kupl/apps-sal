def rectangle_rotation(a, b):
    a1 = filter(lambda x: x % 2 == 0, [a // 2 ** 0.5, a // 2 ** 0.5 + 1])[0]
    a2 = filter(lambda x: x % 2 == 1, [a // 2 ** 0.5, a // 2 ** 0.5 + 1])[0]
    b1 = filter(lambda x: x % 2 == 0, [b // 2 ** 0.5, b // 2 ** 0.5 + 1])[0]
    b2 = filter(lambda x: x % 2 == 1, [b // 2 ** 0.5, b // 2 ** 0.5 + 1])[0]
    return a1 * b1 + a2 * b2
