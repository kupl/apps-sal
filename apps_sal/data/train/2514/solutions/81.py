class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for i in arr1:
            a = 1
            for j in arr2:
                if abs(i - j) <= d:
                    a = 0
            result += a
        return result
