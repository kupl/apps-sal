class Solution:

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        m1 = m2 = m3 = -2 ** 32
        for v in nums:
            if v == m1 or v == m2 or v == m3:
                continue
            if v > m1:
                (m1, m2, m3) = (v, m1, m2)
            elif v == m1 or v > m2:
                (m2, m3) = (v, m2)
            elif v == m2 or v > m3:
                m3 = v
        return m3 if m3 > -2 ** 32 else max(nums)
