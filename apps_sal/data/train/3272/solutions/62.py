def find_average(nums):
    sum = 0
    for n in nums:
        sum += n
    if len(nums) == 0:
        return 0
    sum /= len(nums)
    return sum
