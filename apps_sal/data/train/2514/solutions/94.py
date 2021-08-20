class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for a in arr1:
            add = True
            for b in arr2:
                if abs(a - b) <= d:
                    add = False
            if add:
                res += 1
        return res
