from functools import reduce


def remove_duplicate_words(s):
    return reduce(lambda res, curr: res if curr in res else res + ' ' + curr, s.split(), '').lstrip()
