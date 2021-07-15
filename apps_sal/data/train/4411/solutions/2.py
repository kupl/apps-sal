def find_missing_number(nums):
    return sum(range(1,len(nums)+2))-sum(nums)
