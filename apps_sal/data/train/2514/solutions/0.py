class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in arr1:
            flag = 0
            for j in arr2:
                if abs(i - j) <= d:
                    flag = 1
                    break
            if flag == 0:
                count += 1
        return count
