class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return []
        if n == 2:
            return A[0]
        A.sort()
        for i in range(n):
            if A[i] == A[i + 1]:
                return A[i]
