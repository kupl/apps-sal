import itertools


def solve(arr):
    n = 0
    nums = set(arr)
    for com in itertools.combinations(arr, 2):
        diff = com[1] - com[0]
        if (com[1] + diff in nums):
            n += 1
    return n
