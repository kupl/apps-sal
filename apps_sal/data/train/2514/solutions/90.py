class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        boss = 0
        for val1 in arr1:
            cnt = 0
            for val2 in arr2:
                if abs(val2 - val1) <= d:
                    cnt += 1
            if cnt == 0:
                boss += 1
        return boss
