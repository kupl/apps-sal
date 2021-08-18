class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in arr1:
            yes = 0
            for j in arr2:
                if abs(i - j) <= d:
                    yes = 1
            if(yes == 1):
                count += 1
        return len(arr1) - count
