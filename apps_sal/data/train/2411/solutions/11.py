class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        R = []

        for n in nums:
            if n not in R:
                if len(R) < 3:
                    R.append(n)
                elif min(R) < n:
                    R.remove(min(R))
                    R.append(n)
                R = sorted(R)
        return R[0] if len(R) == 3 else max(R)
