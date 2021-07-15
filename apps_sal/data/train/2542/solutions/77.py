class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        ans=True
        n=len(A)
        if n<=2:
            return ans
        # ind=0
        # while True:
        #     if ind+1==n:
        #         break
        #     else:
        #         if A[ind]<A[ind+1]:
        #             comp=\"<\"
        #             break
        #         elif A[ind]>A[ind+1]:
        #             comp=\">\"
        #             break
        #         else:
        #             ind+=1
        # for j in range(ind,n-1):
        #     if  not eval(\"A[j]\"+comp+\"=A[j+1]\"):
        #                  return False
        # return ans
        left=True
        right=True
        for i in range(1,n):
            if A[i]>A[i-1]:
                left=False
                break
        for i in range(1,n):
            if A[i]<A[i-1]:
                right=False
                break
        return left or right
        
            
            

