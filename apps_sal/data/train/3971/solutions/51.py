def tidyNumber(n):
    nums = [int(num) for num in str(n)]
    srted = sorted(nums)
    if nums == srted:
        return True 
    else:     
        return False
