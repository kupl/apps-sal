class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0:
            return 0

        unique = {}
        for num in nums:
            unique[num] = unique.get(num, 0) + 1

        res = 0
        for num in unique:
            if k == 0:
                if unique[num] > 1:
                    res += 1
            else:
                if num + k in unique:
                    res += 1

        return res
