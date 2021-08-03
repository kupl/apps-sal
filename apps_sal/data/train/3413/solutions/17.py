def solution(nums):
    if nums == None:
        return []
    if len(nums) == 0:
        return []
    low = nums[0]
    other = nums[1:].copy()
    mlist = solution(other)
    niggers = []
    for i in mlist:
        if i < low:
            niggers.append(i)
    p = 0
    if len(niggers) != 0:
        p = min(niggers)
    mlist.insert(p, low)
    return mlist
