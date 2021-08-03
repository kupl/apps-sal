class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A) < 3):
            return False
        elif(A.index(max(A)) == 0 or A.index(max(A)) == (len(A) - 1)):
            return False
        else:
            for i in range(A.index(max(A))):
                if(A[i] >= A[i + 1]):
                    return False
            for i in range(A.index(max(A)), len(A) - 1):
                if(A[i] <= A[i + 1]):
                    return False
            return True
