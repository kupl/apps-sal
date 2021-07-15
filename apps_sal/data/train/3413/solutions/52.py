def solution(nums: list) -> list:
    if nums != None:
        length = len(nums)
        if length > 0:
            return sorted(nums)
        else:
            return []
    else:
        return []
