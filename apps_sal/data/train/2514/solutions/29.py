class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        val = 0
        dist = 0
        for i in range(0, len(arr1)):
            for j in range(0, len(arr2)):
                if abs(arr1[i] - arr2[j]) > d:
                    val += 1
                else:
                    break
            if val == len(arr2):
                dist += 1
            val = 0
        return dist
