def find_average(nums):
    try:
        return sum(nums) * 1.0 / len(nums)
    except:
        return 0
