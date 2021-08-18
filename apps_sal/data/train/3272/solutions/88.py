def find_average(nums):
    print(nums)
    items = 0
    total = 0.0
    for a in nums:
        items += 1
        total += a
    return 0 if items == 0 else total / items
