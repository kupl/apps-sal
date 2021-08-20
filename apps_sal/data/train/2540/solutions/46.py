class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        while len(A) >= 3:
            if A[1] + A[2] > A[0]:
                return A[1] + A[2] + A[0]
            A.pop(0)
        return 0
