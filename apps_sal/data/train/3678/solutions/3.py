def code(x, y):
    return sum(int('9' * len(str(n))) for n in [x, y]) - x - y
