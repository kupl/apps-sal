class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = 0
        c1 = 0
        for a in arr1:
            for r in arr2:
                if abs(a - r) > d:
                    c1 += 1
            if c1 == len(arr2):
                c += 1
            c1 = 0
        return c
