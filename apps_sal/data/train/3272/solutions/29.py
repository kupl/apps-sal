def find_average(nums):
    a = sum(nums)
    b = len(nums)
    
    if (a == 0) or (b == 0):
        return 0
    else:
        return(a/b)
