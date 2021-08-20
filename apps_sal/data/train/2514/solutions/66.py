class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for i in arr1:
            found = True
            for j in arr2:
                if j > i + d:
                    break
                elif abs(i - j) <= d:
                    found = False
                    break
            res += found
        return res
