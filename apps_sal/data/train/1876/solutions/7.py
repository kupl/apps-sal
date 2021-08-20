class Solution:

    def reachNumber(self, t):
        """
        :type target: int
        :rtype: int
        """
        t = abs(t)
        (lo, hi) = (1, t)
        while lo < hi:
            m = (lo + hi) // 2
            val = m * (m + 1) // 2
            if val < t:
                lo = m + 1
            else:
                hi = m
        sm = lo * (lo + 1) // 2
        ans = lo
        while (sm - t) % 2 != 0:
            ans += 1
            sm += ans
        return ans
