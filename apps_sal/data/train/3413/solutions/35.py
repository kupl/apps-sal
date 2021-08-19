def solution(nums):
    if type(nums) != list:
        return []
    if len(nums) == 0:
        return []
    return sorted(nums)
