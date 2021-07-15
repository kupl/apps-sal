def summary_ranges(nums):
    if not nums: return []
    
    r, s, l = [], nums[0], nums[0]
    for n in nums:
        if n - l > 1:
            r.append(str(s)+'->'+str(l) if s != l else str(s))
            s = n
        l = n
    r.append(str(s)+'->'+str(l) if s != l else str(s))
    return r
