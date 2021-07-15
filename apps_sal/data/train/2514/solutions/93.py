class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        ans = 0
        
        for a in arr1:
            isGood = True
            
            for b in arr2:
                if (abs(a-b)<=d):
                    isGood = False
                    break
            
            if (isGood): 
                ans += 1
        
        return ans
                

