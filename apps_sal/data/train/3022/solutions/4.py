def two_highest(l):
    if type(l) != list:
        return False
    return sorted(list(set(l)), key=lambda k: -k)[:2]
