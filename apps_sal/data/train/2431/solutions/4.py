class Solution:

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        (result, lookup) = (set(), set())
        for num in nums:
            if num + k in lookup:
                result.add(num)
            if num - k in lookup:
                result.add(num - k)
            lookup.add(num)
        return len(result)
