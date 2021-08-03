class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        p = 0
        for i in range(len(A) - 2):
            if A[i] < sum(A[i + 1:i + 3]):
                p = sum(A[i:i + 3])
                break
        return p
