def tidyNumber(n):
    print(n)
    nums = [int(x) for x in str(n)]
    
    for m,i in enumerate(nums[:-1]):
        if i<=nums[m+1]:
            continue
        else:
            return False
    return True        
