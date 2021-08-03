class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        ret = 0
        for i in count:
            if i + 1 in count:
                ret = max(ret, count[i] + count[i + 1])

        return ret
