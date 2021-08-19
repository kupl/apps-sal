class Solution:

    def findPairs(self, nums, k):
        """ Returns number of unique k-diff pairs(i, j) such as |i - j| = k.
        Algorithm based on hashing.

        Time complexity: O(n). Space complexity: O(n), n is len(nums).
        """
        num_count = dict()
        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1
        total = 0
        for n in num_count:
            if k == 0 and num_count[n] > 1:
                total += 1
            elif k > 0 and n + k in num_count:
                total += 1
        return total
