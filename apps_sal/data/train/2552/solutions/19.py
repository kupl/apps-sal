class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        x = len(arr) / 4
        i = 0
        while i < len(arr):
            y = arr.count(arr[i])
            if y > x:
                return arr[i]
            i += y
