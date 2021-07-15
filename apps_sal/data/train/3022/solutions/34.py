def two_highest(arg1):
    r = sorted(list(set(arg1)), reverse=True)
    return r[:2]
