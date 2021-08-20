from collections import defaultdict


def merge(*dcts):
    result = defaultdict(list)
    for dct in dcts:
        for (k, v) in list(dct.items()):
            result[k].append(v)
    return result
