from itertools import groupby


def london_city_hacker(journey):
    return f'£{sum((2.4 * len(list(l)) if k is str else (len(list(l)) + 1) // 2 * 1.5 for (k, l) in groupby(journey, type))):.2f}'
