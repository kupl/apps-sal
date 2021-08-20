def find_average(nums):
    sum = 0
    for n in nums:
        sum += n
    if len(nums) == 0:
        avg = 0
    else:
        avg = sum / len(nums)
    return avg
