def solution(nums=[]):
    try:
        if len(nums) > 0:
            nums.sort()
            return nums
        elif len(nums) == 0:
            return []
    except:
        return []
