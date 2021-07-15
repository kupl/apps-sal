class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i:i+3][1] + A[i:i+3][2] > A[i:i+3][0]:
                return sum(A[i:i+3])
        return 0
