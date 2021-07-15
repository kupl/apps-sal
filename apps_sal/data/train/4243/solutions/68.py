def find_average(nums):
    sum = 0
    for i in nums:
        sum += i
    total = sum / len(nums)
    return total
