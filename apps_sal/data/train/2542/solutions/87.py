class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i = 0
        j = 1
        if(A.index(min(A)) == 0 or A.index(min(A)) == (len(A) - 1) or min(A) == A[-1]):
            if(A.index(min(A)) == 0):
                while j <= len(A) - 1:
                    if(A[i] <= A[j]):
                        i = i + 1
                        j = j + 1
                    else:
                        return False
            elif(A.index(min(A)) == len(A) - 1 or min(A) == A[-1]):
                while j <= len(A) - 1:
                    if(A[i] >= A[j]):
                        i = i + 1
                        j = j + 1
                    else:
                        return False
        else:
            return False
        return True
