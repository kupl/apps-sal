class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A)==0 or len(A)==1:
            return 0
        A.sort()
        cnt=0
        for i in range(1,len(A)):
            if A[i-1]>=A[i]:
                temp=A[i]
                A[i]=A[i-1]+1
                cnt+=A[i]-temp
        print(A)
        return cnt
