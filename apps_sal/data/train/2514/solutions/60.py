class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        l = len(arr2)
        arr2.sort()
        for i in arr1:
            temp_count = 0
            for j in arr2:
                if(abs(i-j) <= d):
                    break
                else:
                    temp_count += 1
            if(temp_count == l):
                count += 1
            temp_count = 0
        return count 
