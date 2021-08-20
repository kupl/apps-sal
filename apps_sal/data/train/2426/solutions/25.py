class Solution:

    def smallestRangeI(self, a: List[int], k: int) -> int:
        a = sorted(a)
        a[-1] = max(a)
        a[0] = min(a)
        if a[-1] - k <= a[0] + k:
            return 0
        return a[-1] - k - (a[0] + k)
