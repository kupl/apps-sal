def solution(nums):
    if not nums or len(nums) == 0:
        return []
    sorted = nums.copy()
    sorted.sort()
    return sorted
