from collections import defaultdict


def group_in_10s(*nums):
    dct = defaultdict(list)
    for n in sorted(nums):
        dct[n // 10].append(n)
    return [dct.get(i) for i in range(max(dct) + 1)] if nums else []
