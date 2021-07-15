class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for n in arr:
            if arr.count(n)/len(arr) > 0.25:
                return n
