class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        t=list(set([i for i in range(1,3000)])-set(arr))
        t.sort()
        return t[k-1]
        
        
                
            

