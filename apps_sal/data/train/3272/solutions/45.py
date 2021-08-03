def find_average(nums):
    total = 0
    for i in nums:
        total += i
    if nums:
        return total / len(nums)
    else:
        return 0
