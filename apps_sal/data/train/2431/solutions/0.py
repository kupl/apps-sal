class Solution:

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        if k < 0:
            return count
        if k == 0:
            new_nums = collections.defaultdict(int)
            for i in nums:
                new_nums[i] += 1
            for value in new_nums:
                if new_nums[value] > 1:
                    count += 1
            return count
        if k > 0:
            nums = set(nums)
            for i in nums:
                if i + k in nums:
                    count += 1
            return count
