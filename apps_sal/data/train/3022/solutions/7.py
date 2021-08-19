def two_highest(x):
    if type(x) is list:
        return [] if len(x) == 0 else sorted(list(set(x)))[::-1][:2]
    return False
