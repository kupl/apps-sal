def shift_left(a, b):
    for i in range(len(b)):
        if a.endswith(b[i:]):
            return len(a) + len(b) - 2 * len(b[i:])
    return len(a) + len(b)
