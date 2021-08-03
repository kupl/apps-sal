def find_average(nums):
    sum = 0
    if len(nums) > 0:
        for i in nums:
            sum += i
        return sum / len(nums)
    else:
        return 0
