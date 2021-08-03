class Solution:
    def isMonotonic(self, a: List[int]) -> bool:
        n = len(a)
        std = 0
        for i in range(0, n - 1):

            sgn = a[i] - a[i + 1]

            if sgn == 0:
                continue

            sgn = abs(sgn) / sgn
            if std == 0:
                std = sgn
            if sgn != std and sgn != 0:
                return False

        return True
