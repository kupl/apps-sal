class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max3, max2, max1 = float("inf"), float("inf"), float("inf")

        for num in nums:
            carry = num

            if max3 == carry or max2 == carry or max1 == carry:
                continue

            if max3 == float("inf"):
                max3 = carry
                continue
            else:
                if max3 < carry:
                    max3, carry = carry, max3

            if max2 == float("inf"):
                max2 = carry
                continue
            else:
                if max2 < carry:
                    max2, carry = carry, max2

            if max1 == float("inf"):
                max1 = carry
                continue
            else:
                if max1 < carry:
                    max1 = carry

        print((max3, max2, max1))

        return max1 if max1 != float("inf") else max3
