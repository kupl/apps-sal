class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        N = len(A) - 1
        reached = False
        for i in range(N):
            if A[i] == A[i + 1]:
                return False

            if not reached:
                if A[i] > A[i + 1]:
                    if i == 0:
                        return False
                    reached = True
            else:
                if A[i] < A[i + 1]:
                    return False
        return reached
