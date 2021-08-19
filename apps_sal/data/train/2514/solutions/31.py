class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distanceValue = 0
        for i in range(len(arr1)):
            val = arr1[i]
            shouldCount = True
            for j in range(len(arr2)):
                if abs(val - arr2[j]) <= d:
                    shouldCount = False
                    break
            if shouldCount == True:
                distanceValue += 1
        return distanceValue
