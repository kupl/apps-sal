class Solution:
    def missingNumber(self, array):
        """ Time complexity: O(n). Space complexity: O(1).
        """
        n = len(array)
        for i, num in enumerate(array):
            n = n ^ i ^ num
        return n
