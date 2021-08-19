def find_average(nums):
    if len(nums) == 0:
        return 0
    sums = sum(nums)
    avg = sums / len(nums)
    return avg
