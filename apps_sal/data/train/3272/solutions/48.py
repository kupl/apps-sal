def find_average(nums):
    if len(nums) < 1:
        return 0
    else:
        return sum(nums) / len(nums)
