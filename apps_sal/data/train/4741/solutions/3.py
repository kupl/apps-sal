from re import findall


def pseudo_sort(st):
    lows = sorted(findall(r'\b[a-z]+\b', st))
    ups = sorted(findall(r'[A-Z][A-Za-z]*', st), reverse=True)
    return ' '.join(lows + ups)
