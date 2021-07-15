class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        
        arr2.sort()
        
        for i in range(len(arr1)):
            
            flag = True
            
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = False
                    break
                    
            if flag:
                ans += 1
                
        return ans
