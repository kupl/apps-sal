def solution(nums):
    l = []
    if nums == [] or nums == None:
        return []
    while nums:
        l.append(min(nums))
        nums.remove(min(nums))
    return l
