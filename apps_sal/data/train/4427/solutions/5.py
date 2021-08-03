from itertools import groupby


def sum_groups(arr):
    nums = list(arr)
    while True:
        tmp = [sum(g) for _, g in groupby(nums, key=lambda a: a % 2)]
        if nums == tmp:
            return len(nums)
        nums = tmp
