class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if self.checkMonInc(A, n) or self.checkMonDec(A, n):
            return True
        return False

    def checkMonInc(self, A, n):
        for i in range(1, n):
            if A[i] >= A[i - 1]:
                continue
            else:
                return False
        return True

    def checkMonDec(self, A, n):
        for i in range(1, n):
            if A[i] <= A[i - 1]:
                continue
            else:
                return False
        return True
