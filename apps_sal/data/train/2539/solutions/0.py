class Solution:

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return 0
        array = sorted(nums)
        for i in range(len(array)):
            try:
                dif = array[i + 1] - array[i]
                if dif != 1:
                    return array[i] + 1
            except:
                return array[-1] + 1
