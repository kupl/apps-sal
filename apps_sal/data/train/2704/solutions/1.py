def is_increasing_sequence(a):
    return all((x < y for (x, y) in zip(a, a[1:])))


def almost_increasing_sequence(a):
    return any((is_increasing_sequence(a[:i] + a[i + 1:]) for i in range(len(a))))
