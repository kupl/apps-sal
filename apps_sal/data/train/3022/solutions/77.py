def two_highest(arg1):
    return sorted((x for x in set(arg1)), key=int)[::-1][:2]
