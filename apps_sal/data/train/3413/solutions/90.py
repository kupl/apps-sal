#More elegant:
def solution(nums):
    return (sorted(nums) if nums is not None else [])


#More detailed:
def solution(nums):
    if nums is None:
        return []
    else:
        #nums.sort()
        return sorted(nums)
