def find_average(nums):
    try:
        return sum(nums)/len(nums)
    except ZeroDivisionError as ak:
        return 0

