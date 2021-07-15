class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        len_25 = len(arr) * .25
        for item in set(arr):
            if arr.count(item) > len_25:
                return item
