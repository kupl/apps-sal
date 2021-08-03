def find_average(nums):
    if nums == []:
        return 0
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    return sum / len(nums)
