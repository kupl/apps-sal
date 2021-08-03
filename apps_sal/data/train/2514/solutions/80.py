class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        r = 0
        for i in arr1:
            ir = 1
            for j in arr2:
                if abs(i - j) <= d:
                    ir = 0
                    continue
            r += ir
        return r
