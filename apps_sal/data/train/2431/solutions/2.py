class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        count = 0
        list_nums = set(nums)
        if k == 0:
            nums = collections.Counter(nums)
            for each in nums:
                if nums[each] > 1:
                    count += 1
            return count
        elif k < 0:
            return 0
        elif k > 0:
            for i in list_nums:
                if i + k in list_nums:
                    count += 1
            return count
