class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        high=arr[-1]
        for i in range(1,high+1):
            if(i not in arr):
                k-=1
            if(k==0):
                return i
        if(k>0):
            return high+k

