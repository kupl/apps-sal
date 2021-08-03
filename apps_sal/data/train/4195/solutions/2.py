from itertools import chain, groupby


def merge_group(grp):
    xs = list(grp)
    q, r = divmod(len(xs), 2)
    return [xs[0] * 2] * q + [xs[0]] * r


def merge(line):
    n = len(line)
    line = list(filter(None, line))
    line = list(chain.from_iterable(merge_group(grp) for _, grp in groupby(line)))
    return line + [0] * (n - len(line))
