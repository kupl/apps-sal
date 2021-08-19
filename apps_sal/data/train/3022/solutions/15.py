def two_highest(list):
    if len(list) < 0:
        return []
    elif len(list) > 0 and (not str(list[0]).isdigit()):
        return False
    return sorted(set(list))[::-1][0:2]
