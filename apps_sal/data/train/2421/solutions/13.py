class Solution:
    def majorityElement(self, nums):

        ele = {}
        for i in nums:
            if i in ele:
                ele[i] += 1
            else:
                ele[i] = 1

            if ele[i] > (len(nums) / 2):
                return int(i)
        """
         :type nums: List[int]
         :rtype: int
         """
