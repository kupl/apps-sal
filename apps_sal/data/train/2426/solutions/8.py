class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        avg = round((min(A) + max(A)) / 2)
        mn, mx = float('Inf'), float('-Inf')
        for n in A:
            d = min(K, abs(avg - n))
            n += d * (-1 if n > avg else 1)
            mn, mx = min(mn, n), max(mx, n)

        return mx - mn
