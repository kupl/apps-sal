def find_average(nums):
    # your code here
    total = 0
    for num in nums:
        total += num
    return total / (len(nums) if len(nums) > 0 else 1)
