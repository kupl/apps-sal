
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        val = len(arr) * 0.25
        for i in set(arr):
            if arr.count(i) > val:
                return i
                break
