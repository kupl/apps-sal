class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        up = True
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                return False
            if up:
                if A[i] < A[i - 1]:
                    if i == 1:
                        return False
                    up = False
            elif A[i] > A[i - 1]:
                return False
        return not up
