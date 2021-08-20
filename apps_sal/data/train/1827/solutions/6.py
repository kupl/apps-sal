class Solution:

    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        return self.use_binary_search(n)

    def use_math(self, n):
        n = int(n)
        max_m = int(math.log(n, 2))
        for m in range(max_m, 1, -1):
            k = int(n ** m ** (-1))
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)

    def use_binary_search(self, n):
        n = int(n)
        for d in range(60, 0, -1):
            if 1 << d < n:
                base = self.binary_search(n, d)
                if base:
                    return str(base)
        return str(n - 1)

    def binary_search(self, n, d):
        (lo, hi) = (1, int(pow(n, 1.0 / d) + 1))
        while lo < hi:
            mid = lo + (hi - lo) // 2
            total = 1
            for i in range(1, d + 1):
                total += mid ** i
            if total == n:
                return mid
            elif total < n:
                lo = mid + 1
            else:
                hi = mid
        return 0
