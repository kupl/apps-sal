class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        front = nums[0]
        for i in range(1, len(nums)):
            print(front)
            if front > nums[i]:
                if count > 0:
                    return False
                else:
                    if i > 1 and nums[i - 2] > nums[i]:
                        front = nums[i - 1]
                    else:
                        front = nums[i]
                    count += 1
            else:
                front = nums[i]
        return True
