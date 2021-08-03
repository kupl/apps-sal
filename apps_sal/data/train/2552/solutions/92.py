class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0.25 * len(arr)
        arr1 = list(set(arr))
        for ele in arr1:
            if arr.count(ele) > count:
                return ele
