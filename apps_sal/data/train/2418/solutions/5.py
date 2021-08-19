class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dic = {}
        # for i in range(len(nums)):
        #     if nums[i] in dic.keys():
        #         return True
        #     dic[nums[i]] = i
        # return False
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
