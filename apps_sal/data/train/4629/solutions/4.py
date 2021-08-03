import functools


def penalty(lis):
    def custom(i, j): return -1 if str(j) + str(i) > str(i) + str(j) else 1
    res = sorted(lis, key=functools.cmp_to_key(custom))
    return "".join(map(str, res))
