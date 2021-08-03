from math import sqrt
from typing import List


class Solution:
    def findDivisor(self, num):
        min_gap = num
        min_gap_saved = []
        for i in range(int(sqrt(num)), 0, -1):
            if num % i == 0:
                gap = abs(i - num // i)
                if gap < min_gap:
                    min_gap = gap
                    min_gap_saved = sorted([i, num // i])
        return min_gap_saved

    def closestDivisors(self, num: int) -> List[int]:
        a, b = self.findDivisor(num + 1)
        c, d = self.findDivisor(num + 2)
        if b - a > d - c:
            return [c, d]
        else:
            return [a, b]


s = Solution()
print((s.closestDivisors(8)))
print((s.closestDivisors(123)))
print((s.closestDivisors(999)))
print((s.closestDivisors(170967091)))
