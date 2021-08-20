class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        i = 0
        n = len(A)
        while i < n - 1 and A[i] == A[i + 1]:
            i += 1
        if i == n - 1:
            return True
        if A[i] > A[i + 1]:
            while i < n - 1 and A[i] >= A[i + 1]:
                i += 1
            if i != n - 1:
                return False
            else:
                return True
        else:
            while i < n - 1 and A[i] <= A[i + 1]:
                i += 1
            if i != n - 1:
                return False
            else:
                return True
