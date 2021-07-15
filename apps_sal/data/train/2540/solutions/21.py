class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)
        i = len(A)-1
        while i>=2:
            if A[i-2]+A[i-1]>A[i]: return A[i-2]+A[i-1]+A[i]
            i -= 1
        return 0
