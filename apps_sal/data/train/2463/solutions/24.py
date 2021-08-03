class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        switch = 0
        if A[0] > A[1]:
            return False
        for i in range(2, len(A)):
            if A[i] == A[i - 1]:
                return False
            if switch == 0 and A[i] < A[i - 1]:
                switch = 1
            elif switch == 1 and A[i] > A[i - 1]:
                return False
        if switch == 0:
            return False
        return True
