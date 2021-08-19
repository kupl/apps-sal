class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        for i in range(1, len(A)):
            if i > 0 and A[i] <= A[i - 1]:
                target = A[i - 1] + 1
                ans += target - A[i]
                A[i] = target
        return ans
