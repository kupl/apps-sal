class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for item in set(arr):
            l = len(arr)
            if arr.count(item) > l / 4:
                return item
