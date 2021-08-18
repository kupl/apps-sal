class Solution:
    def findUnsortedSubarray(self, nums):
        """ Improved algorithm.
        Time complexity: O(n). Space complexity: O(1).
        """
        n = len(nums)
        if n < 2:
            return 0

        left = n - 1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                left = i + 1
                break
        min_i = left
        for i in range(left + 1, n):
            if nums[i] < nums[min_i]:
                min_i = i

        right = 0
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                right = i - 1
                break
        max_i = right
        for i in range(max_i - 1, -1, -1):
            if nums[i] > nums[max_i]:
                max_i = i

        for i in range(min_i):
            if nums[i] > nums[min_i]:
                min_i = i
                break

        for i in range(n - 1, max_i, -1):
            if nums[i] < nums[max_i]:
                max_i = i
                break

        length = max_i - min_i + 1
        return length if length > 0 else 0
