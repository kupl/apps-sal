class Solution:

    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        flag = 0
        for i in range(len(nums)):
            if flag == 0:
                if i == len(nums) - 1:
                    return nums[i]
                if nums[i] == nums[i + 1]:
                    flag = 1
                else:
                    return nums[i]
            else:
                flag = 0
                continue
