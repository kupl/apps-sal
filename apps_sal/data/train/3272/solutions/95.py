def find_average(nums):
    if len(nums) == 0:
        return 0
    else:
        total = sum(nums)
        avg = total / len(nums)
        return avg
