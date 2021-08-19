class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = len(arr) * 0.25
        for i in arr:
            if arr.count(i) > cnt:
                return i
