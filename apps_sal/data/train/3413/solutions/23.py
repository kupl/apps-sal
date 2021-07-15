def solution(nums):
    if nums is None:
        return []
    sorted_nums = sorted(nums)
    if len(sorted_nums) > 0:
        return sorted_nums
    else:
        return []
