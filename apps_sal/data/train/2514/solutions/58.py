class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        total = 0
        
        arr1.sort()
        arr2.sort()
        
        for i in arr1:
            for j in arr2:
                if abs(i-j) <= d:
                    total -=1
                    break
            total += 1
        
        return total
