class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x=len(arr)/4
        for i in arr:
            y=arr.count(i)
            if y>x:
                return i
    
        
        
        

