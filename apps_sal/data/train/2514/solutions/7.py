class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        fcnt = 0
        lnb = len(arr2)
        for a in arr1:
            cnt = 0
            for b in arr2:
                if abs(a - b) > d:
                    cnt = cnt + 1
            if cnt == lnb:
                fcnt = fcnt + 1
        return fcnt
