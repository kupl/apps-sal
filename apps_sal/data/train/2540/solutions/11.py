class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            a = A[i]
            b = A[i - 1]
            c = A[i - 2]
            if a < b + c:
                return a + b + c
        return 0
