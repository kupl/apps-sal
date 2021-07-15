class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        climb = True
        cs = 0
        fs = 0
        for i in range(1, len(A)):
            if climb == True:
                if A[i] > A[i-1]:
                    cs += 1
                    continue
                elif A[i] == A[i-1]:
                    return False
                else:
                    climb = False
            if climb == False:
                if A[i] < A[i-1]:
                    fs += 1
                    continue
                else:
                    return False
        if cs > 0 and fs > 0:
            return True
        return False
