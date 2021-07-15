def two_highest(arg1):
    x = [i for i in arg1 if isinstance(i, str)]
    if len(x) > 0:
        return False
    if len(arg1) == 0:
        return []
    return sorted(list(set(arg1)))[-2:][::-1]
