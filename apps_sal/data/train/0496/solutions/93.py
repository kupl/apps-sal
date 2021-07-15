class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        current=0
        res=0
        for i in range(len(A)):
            if A[i]<=current:
                res+=current-A[i]
                current=current+1
            else:
                current=A[i]+1
        return res

