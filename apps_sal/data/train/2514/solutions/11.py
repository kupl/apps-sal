class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = 0
        l2 = len(arr2)
        for i in arr1:
            tmp = 0
            for j in arr2:
                if abs(i - j) > d:
                    tmp += 1
            if tmp == l2:
                c += 1
        return c
