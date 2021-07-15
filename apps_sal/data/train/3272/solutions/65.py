def find_average(nums):
    sum = 0
    if len(nums) == 0:
        return 0
    else:
        for i in nums:
            sum += i
    return sum / len(nums)
