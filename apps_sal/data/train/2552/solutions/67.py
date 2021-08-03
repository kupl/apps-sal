class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) // 4
        for i in arr:
            if arr.count(i) > n:
                return i
