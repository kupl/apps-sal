class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        i = 0
        while i < len(A) - 2:
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
            else:
                i = i + 1
        return 0
