def solution(nums):
    if nums == None:
        return []
    elif len(nums) < 1:
        return []
    else:
        return sorted(nums)
