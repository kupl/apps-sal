def solution(nums, default=None):
    if nums:
        nums.sort()
        return nums
    else:
        nums = []
        return  nums
