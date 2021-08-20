def number(b):
    return sum((e[0] for e in b)) - sum((e[1] for e in b))
