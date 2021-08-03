class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A = sorted(A)
        ans = 0
        if len(A) == 0:
            return 0
        prev = A[0]
        i = 1
        while i < len(A):
            if A[i] <= prev:
                ans += prev - A[i] + 1
                prev += 1
            else:
                prev = A[i]
            i += 1
        return ans
