from functools import lru_cache


@lru_cache(maxsize=16384)
def partition_helper(sum, largest_number):
    if largest_number == 0:
        return 0
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    return partition_helper(sum, largest_number - 1) + partition_helper(sum - largest_number, largest_number)


def partitions(n): return partition_helper(n, n)
