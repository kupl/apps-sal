def diff(a, b):
    return sorted(list(set(a).symmetric_difference(set(b))))
