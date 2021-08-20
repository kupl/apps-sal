def solution(nums):
    if nums == None:
        return []
    else:
        nums = list(set(nums))
        nums.sort()
        return nums
