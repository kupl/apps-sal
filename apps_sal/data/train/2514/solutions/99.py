class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        count=0
        for i in arr1:
            a = True
            for j in arr2:
                a=a & (abs(i-j)>d)
            if a==True:
                count+=1
        return count 
