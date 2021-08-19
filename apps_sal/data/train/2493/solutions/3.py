class Solution:
    def maximumProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Easy way to do it: sort them, take top 3 product
        # But have to think about negative numbers, lowest
        # 2 could be 2 giant negatives.. * biggest positive
        # which could still be biggest product

        nums.sort()
        top = nums[~0] * nums[~1] * nums[~2]
        bottom = nums[0] * nums[1] * nums[~0]
        return max(top, bottom)
        # Time O(nlogn) due to sorting
        # Space O(1)

    def maximumProduct(self, nums):
        # Other approach is keep track of min1/2
        # and max1/2/3 while we iterate through the array
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')

        for n in nums:
            if n <= min1:
                min1, min2 = n, min1
            elif n <= min2:
                min2 = n

            if n >= max1:
                max1, max2, max3 = n, max1, max2
            elif n >= max2:
                max2, max3 = n, max2
            elif n >= max3:
                max3 = n

        return max(min1 * min2 * max1, max1 * max2 * max3)
