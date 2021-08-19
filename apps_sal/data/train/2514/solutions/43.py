class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_value = []
        for i in arr1:
            valid = True
            for j in arr2:
                if abs(i - j) <= d:
                    valid = False
                    break
            if valid:
                distance_value.append(i)
        return len(distance_value)
