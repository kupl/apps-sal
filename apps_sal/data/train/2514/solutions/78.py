class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance = 0
        for i in arr1:
            is_there = False
            for j in arr2:
                if abs(i-j)>d:
                    continue
                else:
                    is_there = True
            if not is_there:
                distance+=1
        return distance

