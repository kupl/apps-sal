class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        temp = A[0] 
        res = 0
        for i in range(1, len(A)):
            if A[i] > temp:
                temp = A[i]
            else:
                res += (temp+1-A[i])
                temp += 1
        return res
                
            

