class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        i=len(A)-2
        while(i>=0 and A[i]<=A[i+1]):
            i-=1
        if(i>=0):
            max_=i+1
            # max number greater on right that less than A[i]
            for j in range(max_+1,len(A)):
                if(A[max_]<A[j] and A[j]<A[i]):
                    max_=j
            A[max_],A[i]=A[i],A[max_]

        return A

