def find_average(nums):
    if len(nums) == 0:
        return 0
    s = sum(nums)
    n = s / len(nums)
    return n
