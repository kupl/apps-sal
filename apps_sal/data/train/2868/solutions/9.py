def is_nice(a):
    return all(e + 1 in a or e - 1 in a for e in a) if a else False
