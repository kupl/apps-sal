class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return False
        else:
            t=0
            c1,c2 =0,0
            for i in range(1,len(A)-1):
                if A[i] == A[i+1]:
                    return False
                    break
                elif A[i-1] < A[i] < A[i+1] or A[i-1] > A[i] > A[i+1] or A[i-1] < A[i] > A[i+1]:
                    t +=1
                    if A[i-1] < A[i] < A[i+1]:
                        c1+=1
                    if A[i-1] > A[i] > A[i+1]:
                        c2+=1
            if t ==len(A)-2 and c1< len(A)-2 and c2< len(A)-2:
                return True
            else:
                return False
                    

