from itertools import groupby


def look_and_say_sequence(e, n):
    for i in range(n - 1):
        e = ''.join((f'{len(list(grp))}{key}' for (key, grp) in groupby(e)))
    return e
