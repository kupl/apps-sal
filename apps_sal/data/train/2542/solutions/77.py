class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        ans = True
        n = len(A)
        if n <= 2:
            return ans
        left = True
        right = True
        for i in range(1, n):
            if A[i] > A[i - 1]:
                left = False
                break
        for i in range(1, n):
            if A[i] < A[i - 1]:
                right = False
                break
        return left or right
