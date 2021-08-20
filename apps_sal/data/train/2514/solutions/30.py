class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                temp = arr1[i] - arr2[j]
                if temp < 0:
                    temp = -temp
                if temp <= d:
                    break
                if j == len(arr2) - 1:
                    count += 1
        return count
