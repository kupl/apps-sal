class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for num in arr1:
            greater = True
            for sub in arr2:
                if abs(num-sub) <= d:
                    greater = False
            if greater:
                result += 1
        return result
