class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = len(arr1)
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    c -= 1
                    break
        return c
