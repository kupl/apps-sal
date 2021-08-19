class Solution:

    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        m = 0
        for i in range(len(A) - 2):
            if A[i] + A[i + 1] > A[i + 2] and A[i + 2] + A[i + 1] > A[i] and (A[i + 2] + A[i] > A[i + 1]):
                x = A[i:i + 3]
                if sum(x) > m:
                    m = sum(x)
        return m
