def two_highest(s):
    if type(s) != list:
        return False
    l = list(set(s))
    l.sort(reverse=True)
    return l[:2]
