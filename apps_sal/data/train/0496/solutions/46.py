class Solution:
    def minIncrementForUnique(self, A):
        A.sort()
        ans = 0
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                continue
            ans += A[i - 1] - A[i] + 1
            A[i] = A[i - 1] + 1
        return ans
