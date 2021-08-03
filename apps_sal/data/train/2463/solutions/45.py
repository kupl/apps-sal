class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A or len(A) <= 2:
            return False
        increase = -1
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and increase == -1:
                increase = 1
            if A[i] > A[i - 1] and increase == 1:
                continue
            elif A[i] < A[i - 1] and increase == 1:
                increase = 0
            elif A[i] < A[i - 1] and increase == 0:
                continue
            else:
                return False
        if increase != 0:
            return False
        return True
