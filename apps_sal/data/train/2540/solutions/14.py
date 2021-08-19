class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        for i in range(1, len(A) - 1):
            if A[i - 1] + A[i] <= A[i + 1]:
                continue
            else:
                p = sum(A[i - 1:i + 2])
                ans = max(ans, p)
        return ans
