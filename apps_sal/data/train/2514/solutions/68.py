class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        tot = 0
        for i in arr1:
            found = False
            for j in arr2:
                diff = i - j
                if abs(diff) <= d:
                    found = True
                    break
                if diff <= -d:
                    break
            if not found:
                tot += 1
        return tot
