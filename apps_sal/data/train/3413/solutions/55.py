def solution(nums):
    if type(nums) == list:
        return sorted(nums)
    elif type(nums) != list:
        return []
