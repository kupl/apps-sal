def find_average(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    try:
        per = total / len(nums)
        return per
    except ZeroDivisionError:
        return 0
