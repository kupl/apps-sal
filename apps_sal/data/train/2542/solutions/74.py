class Solution:
    def monotonicArrayIncreasing(self, a):
        i = 0
        while i + 1 < len(a):
            if a[i] > a[i + 1]:
                return False
            i += 1
        return True

    def monotonicArrayDecreasing(self, a):
        i = 0
        while i + 1 < len(a):
            if a[i] < a[i + 1]:
                return False
            i += 1
        return True

    def isMonotonic(self, A: List[int]) -> bool:
        x = self.monotonicArrayDecreasing(A)
        y = self.monotonicArrayIncreasing(A)
        return x or y
