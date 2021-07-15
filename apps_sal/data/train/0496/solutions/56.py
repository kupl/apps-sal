class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) < 2:
            return 0
        A.sort()
        N = len(A)
        res = 0
        start = 0
        for i in range(1,N):
            if A[i] - A[start] >= i - start:
                start = i
            else:
                res += i-start-(A[i]-A[start])
        return res            
                

