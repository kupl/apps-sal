class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        p = 0
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                p = A[i] + A[i + 1] + A[i + 2]
                break
        return p

