class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        direction = 0
        for idx, ele in enumerate(A):
            if idx == 0:
                continue

            if ele > A[idx - 1] and direction == 0:
                direction = 1
            elif ele < A[idx - 1] and direction == 0:
                direction = -1
            elif ele > A[idx - 1] and direction == -1:
                return False
            elif ele < A[idx - 1] and direction == 1:
                return False

        return True
