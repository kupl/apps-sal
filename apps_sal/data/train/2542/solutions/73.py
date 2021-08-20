class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        i = 1
        pr = None
        cur = None
        if len(A) < 3:
            return True
        while i < len(A) - 1:
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                return False
            elif A[i] < A[i - 1] and A[i] < A[i + 1]:
                return False
            elif A[i] >= A[i - 1] and A[i] < A[i + 1] or (A[i] > A[i - 1] and A[i] <= A[i + 1]):
                cur = 'I'
            elif A[i] <= A[i - 1] and A[i] > A[i + 1] or (A[i] < A[i - 1] and A[i] >= A[i + 1]):
                cur = 'D'
            if pr is None and cur is not None:
                pr = cur
            elif pr is not None and cur is not None and (pr != cur):
                return False
            i += 1
        return True
