class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        for (i, x) in enumerate(A):
            if i >= 1:
                if A[i] <= A[i - 1]:
                    ans += A[i - 1] - A[i] + 1
                    A[i] = A[i - 1] + 1
        return ans
