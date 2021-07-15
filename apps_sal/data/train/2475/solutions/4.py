class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        result=0
        M=len(A[0])
        for i in range(M):
            col=[row[i] for row in A]
            if col!=sorted(col):
                result+=1
        return result
            
        

