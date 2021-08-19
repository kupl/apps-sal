from itertools import groupby, chain


def merge(*dicts):
    result = {}
    for d in dicts:
        for (key, value) in d.items():
            result.setdefault(key, []).append(value)
    return result
