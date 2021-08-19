from statistics import mean


def find_average(nums):
    # your code here
    return mean(nums) if len(nums) != 0 else 0
