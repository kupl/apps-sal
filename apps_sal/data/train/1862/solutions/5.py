class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(r):
            l = 0
            while l<r:
                A[l], A[r] = A[r], A[l]
                l, r = l+1, r-1     
                
        ans = []
        for x in range(len(A),0,-1):
            i = A.index(x)+1 #x is the current unsorted largest element
            ans.extend([i, x])
            flip(i-1)
            flip(x-1)
        
        return ans

