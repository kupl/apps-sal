class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for num1 in arr1:
            flag = 1
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    flag = 0
            if flag:
                ans+=1
        return ans                    
        

