class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        up = down = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                up = False
            if A[i] < A[i + 1]:
                down = False

        return up or down
