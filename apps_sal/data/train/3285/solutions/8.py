from re import findall


def trump_detector(t):
    return round(sum(map(lambda a: len(a[1]), findall('([aeiou])(\\1*)', t, 2))) / len(findall('([aeiou])(\\1*)', t, 2)), 2)
