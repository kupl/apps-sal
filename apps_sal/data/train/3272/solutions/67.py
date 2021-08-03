import statistics


def find_average(nums):
    if len(nums) > 0:
        return statistics.mean(nums)
    return 0
