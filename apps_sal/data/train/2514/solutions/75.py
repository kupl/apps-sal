import numpy as np
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res=0
        for num1 in arr1:
            if all(abs(np.subtract(num1,arr2))>d):
                res+=1
        return res
