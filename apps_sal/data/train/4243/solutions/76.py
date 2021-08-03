def find_average(nums):
    count = 0
    total = 0
    for i in nums:
        count += 1
        total += i
    return (total / count)
