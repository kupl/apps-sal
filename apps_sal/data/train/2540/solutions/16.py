class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        Flag = 0
        for i in range(len(A) - 1, 1, -1):
            if A[i] < A[i - 1] + A[i - 2]:
                Flag = 1
                return A[i - 1] + A[i - 2] + A[i]
        if Flag == 0:
            return Flag
