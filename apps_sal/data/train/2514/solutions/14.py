class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        m = len(arr1)
        n = len(arr2)
        distance = 0
        for i in range(m):
            is_valid = True
            for j in range(n):
                if abs(arr1[i] - arr2[j]) <= d:
                    is_valid = False
            if is_valid:
                distance += 1
        return distance
