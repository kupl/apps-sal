def solution(nums):
    if nums:
        nums = [int(x) for x in nums]
        nums.sort()
        return nums
    else:
        return []
