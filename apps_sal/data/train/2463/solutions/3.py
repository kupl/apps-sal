class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        dec = 0
        n = len(A)
        if n < 3:
            return False
        else:
            for i in range(n):
                if i!= 0 and A[i] == A[i-1]:
                    return False
                elif i == 0 and A[i] > A[i+1]:
                    return False
                elif dec == 1 and A[i] > A[i-1]:
                    return False
                elif i != 0 and dec == 0 and A[i] < A[i-1]:
                    dec = 1
                elif i == (n - 1) and dec == 0:
                    return False
            return True
                
                

