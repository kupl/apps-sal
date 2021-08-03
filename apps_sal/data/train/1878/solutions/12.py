class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        s = sorted(arr)

        i = 0
        a_nums = Counter()
        b_nums = Counter()
        total = 0
        while i < len(arr):
            a_nums[arr[i]] += 1
            b_nums[s[i]] += 1
            if a_nums == b_nums:
                a_nums.clear()
                b_nums.clear()
                total += 1
            i += 1

        return total
