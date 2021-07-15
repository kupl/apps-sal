def find_average(nums):
    
    length = len(nums)
    if length == 0:
        return 0
    
    total = sum(nums)
    
    mean = total / length
    
    return mean
