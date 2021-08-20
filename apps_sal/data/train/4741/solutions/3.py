from re import findall


def pseudo_sort(st):
    lows = sorted(findall('\\b[a-z]+\\b', st))
    ups = sorted(findall('[A-Z][A-Za-z]*', st), reverse=True)
    return ' '.join(lows + ups)
