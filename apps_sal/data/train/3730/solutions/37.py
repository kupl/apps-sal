from itertools import cycle


def capitalize(s):
    fss = map(cycle, ((str.upper, str.lower), (str.lower, str.upper)))
    return [''.join(f(c) for f, c in zip(fs, s)) for fs in fss]
