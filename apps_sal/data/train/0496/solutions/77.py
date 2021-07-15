class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A or len(A) == 1:
            return 0
        
        ans = 0
        A.sort()
        for i in range(1,len(A)):
            if A[i-1] >= A[i]:
                gap = abs(A[i-1]-A[i]) + 1
                A[i] += gap
                ans += gap
        return ans
