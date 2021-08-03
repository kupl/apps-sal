from itertools import groupby


def group_in_10s(*args):
    if not args:
        return []
    groups = dict((k, list(xs)) for k, xs in groupby(sorted(args), lambda x: x // 10))
    return [groups.get(i) for i in range(max(groups) + 1)]
