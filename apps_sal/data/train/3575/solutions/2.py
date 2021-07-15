def powerset(nums):
    t = []
    for i in range(2**len(nums)):     
        t.append([nums[k] for k,z in enumerate(bin(i)[2:].zfill(len(nums))) if z =="1"])
    return t
