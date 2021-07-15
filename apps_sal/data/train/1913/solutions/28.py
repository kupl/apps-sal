class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        mid = -1
        for i in range(len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                mid = i
                break
        if mid ==-1:
            return A
        max_mid = -1
        for i in range(mid+1,len(A)):
            if A[mid]>A[i]:
                if A[i]>max_mid:
                    index = i
                    max_mid = A[i]
                #max_mid = max(max_mid,A[i])
        #index = A.index(max_mid)
        A[mid],A[index] = A[index],A[mid]
        return A
