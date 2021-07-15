def array_leaders(nums):
    total,res = sum(nums), []
    for x in nums:
        total -= x
        if x > total: res.append(x)
               
    return res
