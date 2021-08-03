class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        order = dict()
        if len(nums) > 1:
            for i in range(len(nums)):
                if nums[i] in list(order.keys()):
                    order[nums[i]] += 1
                    if order[nums[i]] > (len(nums) // 2):
                        return nums[i]
                else:
                    order[nums[i]] = 1
        else:
            return nums[0]
