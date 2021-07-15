from collections import Counter


def sum_no_duplicates(nums):
    return sum(k for k, v in list(Counter(nums).items()) if v == 1)

