from statistics import mean

def find_average(nums):
    return mean(nums) if len(nums) > 0 else 0
