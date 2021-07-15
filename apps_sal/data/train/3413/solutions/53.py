def solution(nums):
    if not nums:
        return []
    else:
        for x in range(len(nums)):
            for i in range(len(nums) -1):
                if nums[i]>nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
        return nums
