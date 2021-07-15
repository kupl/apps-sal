def pattern(n):
    nums = list(range(1,n+1))
    result = ''
    result += ''.join(str(n) for n in nums)
    
    for i in range(1, n):
        result += '\n'
        nums.append(nums.pop(0))
        result += ''.join(str(n) for n in nums)
        
    return result
    
    

