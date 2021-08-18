class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        i = 0

        while i < n - 1 and A[i] < A[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i < n - 1 and A[i] > A[i + 1]:
            i += 1

        if i != n - 1:
            return False
        return True
