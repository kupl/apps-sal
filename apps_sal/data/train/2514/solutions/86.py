class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for num1 in arr1:
            flag = False
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    flag = True
            if not flag:
                count += 1
        return count
