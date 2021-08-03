# 19
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        nprev = A[0]
        for i in range(1, len(A)):
            if A[i] <= nprev:
                nprev = A[i - 1]
                start = i
                break
            nprev = A[i]
            if i == len(A) - 1:
                return False

        for i in range(start, len(A)):
            if A[i] >= nprev:
                return False
            nprev = A[i]
            if start == 1 and i == len(A) - 1:
                return False
        return True
