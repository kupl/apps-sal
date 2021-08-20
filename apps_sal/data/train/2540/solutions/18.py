class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        a = len(A) - 1
        while a >= 2:
            if A[a] < A[a - 1] + A[a - 2]:
                return A[a] + A[a - 1] + A[a - 2]
            else:
                a -= 1
        return 0
