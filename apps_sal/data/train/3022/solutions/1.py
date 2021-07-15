def two_highest(list):
    return False if isinstance(list, str) else sorted(set(list), reverse=True)[0:2]
