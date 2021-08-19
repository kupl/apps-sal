def two_highest(a):
    return sorted(set(a), reverse=True)[:2] if type(a) is list else False
