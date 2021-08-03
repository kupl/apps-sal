class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr)
        l = l / 4
        for i in arr:
            if arr.count(i) > l:
                return i
