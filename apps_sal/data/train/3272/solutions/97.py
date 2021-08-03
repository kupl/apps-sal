def find_average(nums):
    if len(nums) == 0:
        return 0
    a = 0
    for i in nums:
        a += i
    return a / len(nums)
