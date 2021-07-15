def find_average(nums):
    x = sum(nums)
    y = len(nums)
    if y == 0:
        return 0
    return x / y
