from itertools import groupby


def ones_counter(nums):
    return [sum(1 for b in g) for k, g in groupby(nums) if k]
