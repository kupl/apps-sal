class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        for i in range(1, len(A)):
            if A[i - 1] >= A[i]:
                ans += A[i - 1] - A[i] + 1
                A[i] += A[i - 1] - A[i] + 1

        return ans
