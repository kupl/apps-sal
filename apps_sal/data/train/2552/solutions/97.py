class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr1 = list(set(arr))
        for ele in arr1:
            if arr.count(ele) > (0.25 * len(arr)):
                return ele
