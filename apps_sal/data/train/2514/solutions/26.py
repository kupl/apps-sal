class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:     
        el_num = 0
        
        for i in range(len(arr1)):
            el_num += 1
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    el_num -= 1
                    break
        
        return el_num
