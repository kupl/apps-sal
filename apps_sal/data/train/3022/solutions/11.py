def two_highest(arg1):
    return False if type(arg1) != list else sorted(set(arg1), reverse=True)[:2]
