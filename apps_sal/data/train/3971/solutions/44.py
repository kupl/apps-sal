def tidyNumber(n):
    nums = list(map(int, str(n)))
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
