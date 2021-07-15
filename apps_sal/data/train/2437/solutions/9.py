class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if n<m*k:
            return False
        
        def is_matched(a,b,c):
            if c==0:
                return True
            
            if arr[b:b+m]!=arr[a:a+m]:
                return False
            
            return is_matched(a, b+m, c-1)
        
        for a in range(0, n-k*m+1):
            if is_matched(a, a+m, k-1):
                return True
                
        return False
        

