def solution(nums):
    if nums is None:
        return []
    else:
        return sorted(set(nums))
