class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        # 异或表示相同数为0，索引和数组的数应该两两相对
        for i, x in enumerate(nums):
            res ^= i
            res ^= x
        return res
