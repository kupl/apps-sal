def find_average(nums):
    try:
        a = len(nums)
        b = sum(nums)
        c = b / a
    except:
        return 0
    return c
