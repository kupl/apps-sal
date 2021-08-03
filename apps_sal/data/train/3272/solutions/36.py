def find_average(nums):
    if len(nums) == 0:
        return 0
    sum = 0
    for val in nums:
        sum += val
    return sum / len(nums)
