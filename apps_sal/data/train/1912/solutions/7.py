class Solution:

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        (lo, hi) = (0, len(letters))
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return letters[lo % len(letters)]
