def find_average(nums):
    tot = 0
    mean = 0

    if len(nums) == 0:
        return 0

    for i, number in enumerate(nums):
        tot += number

    mean = tot / len(nums)
    return mean
