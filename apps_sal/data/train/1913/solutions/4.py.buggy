class Solution:
    
        
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A)-2,-1,-1):
            curr=-float(\"inf\")
            k=-1
            for j in range(i+1,len(A)):
                if A[j]>curr and A[j]<A[i]:
                    curr=A[j]
                    # print(curr,A[i],i,j)
                    k=j
            if curr!=-float(\"inf\"):
                # print(\"yo\")
                # print(k,j)
                A[i],A[k]=A[k],A[i]
                return A
        return A
