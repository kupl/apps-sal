class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = int(len(arr) / 4)
        for i in set(arr):
            if arr.count(i) > n:
                return i
