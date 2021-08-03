import functools


def cmp(a, b):
    aa = a.lower()
    bb = b.lower()

    if aa > bb:
        return 1
    elif bb > aa:
        return -1
    else:
        return 0


def sorter(textbooks):
    return sorted(textbooks, key=functools.cmp_to_key(cmp))
