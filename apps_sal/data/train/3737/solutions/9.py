def calc(a):
    return sum((i ** (1, 2)[i > 0] * (1, 3)[idx % 3 == 2] * (1, -1)[idx % 5 == 4] for (idx, i) in enumerate(a)))
