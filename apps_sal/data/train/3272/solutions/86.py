def find_average(nums):
    if not nums:
        return 0
    sum = 0
    quantity = 0
    for value in nums:
        sum = sum + value
        quantity += 1
    return sum / quantity
