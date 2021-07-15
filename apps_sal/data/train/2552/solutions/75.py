class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mark = len(arr) // 4
        for x in arr:
            if mark < arr.count(x):
                return x
