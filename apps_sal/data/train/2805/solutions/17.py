def productFib(prod):
    nums = [0,1]
    i = 0
    status = True
    while status:
        if nums[i]*nums[i+1] <= prod:
            nums.append(nums[i]+nums[i+1])
            i+=1
        else:
            status = False
    i = 0
    while i < len(nums):
        if nums[i]*nums[i+1] == prod:
            return [nums[i],nums[i+1],True]
        elif prod in range(nums[i-1]*nums[i],nums[i]*nums[i+1]):
            return [nums[i],nums[i+1],False]
        i+=1
