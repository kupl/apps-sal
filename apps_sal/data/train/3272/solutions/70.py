def find_average(nums):
    total = sum(nums)
    if len(nums) > 0:
        return total / len(nums)
    return 0
