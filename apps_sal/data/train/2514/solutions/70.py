class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ok = 0
        arr2.sort()
        for test1 in arr1:
            ele = 0
            sign = 0
            for test2 in arr2:
                test = test2 - test1
                if abs(test) <= d:
                    ele = 1
                    break
                if (test > d) or (d < 0):
                    break
            if ele == 0:
                ok += 1
        return ok
