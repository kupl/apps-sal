class Solution:

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            tmp = d.get(nums[i], [])
            tmp.append(i)
            d[nums[i]] = tmp
        low = []
        c = 0
        for k in d:
            tc = len(d.get(k))
            if tc > c:
                c = tc
        for k in d:
            if len(d.get(k)) == c:
                low.append(k)
        result = len(nums)
        for s in low:
            tmp = d.get(s)[-1] - d.get(s)[0] + 1
            if tmp < result:
                result = tmp
        return result
