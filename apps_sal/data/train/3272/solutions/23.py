def find_average(nums):
    try:
        return float(sum(nums)) / len(nums)
    except ZeroDivisionError:
        return 0
