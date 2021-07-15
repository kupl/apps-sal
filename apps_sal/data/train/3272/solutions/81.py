def find_average(nums):
    if len(nums) == 0:
        return 0

    total = 0
    
    for num in nums:
        total+= num
        
    return total/len(nums)
