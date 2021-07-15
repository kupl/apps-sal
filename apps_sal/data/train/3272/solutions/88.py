def find_average(nums):
    print(nums)
    #return [sum(nums)/len(nums) if len(nums)>0 else 0]
    items = 0
    total = 0.0
    for a in nums:
        items += 1
        total += a
    return 0 if items == 0 else total / items

