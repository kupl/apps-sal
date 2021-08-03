def find_average(nums):
    if not nums:
        return 0
    else:
        return sum(nums) / len(nums)
