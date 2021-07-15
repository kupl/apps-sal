class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        print([x for x in arr1 if all (abs(x-y) > d for y in arr2)])
        return len([x for x in arr1 if all (abs(x-y) > d  for y in arr2)])
