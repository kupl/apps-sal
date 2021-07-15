class Solution:
    
    def diff(self, a, b, limit):
        return ( abs(a-b) <= limit ) 
    
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0 
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    
                    if self.diff(arr[i], arr[j], a ) and self.diff(arr[j], arr[k], b) and self.diff(arr[i], arr[k], c):
                        count += 1 
                        
        return count 
                    
                    

