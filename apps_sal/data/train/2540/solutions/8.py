class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        p = 0
        A.sort()
        for i in range(len(A) - 2):
            if A[i] + A[i + 1] > A[i + 2]:
                p = A[i] + A[i + 1] + A[i + 2]
        return p
