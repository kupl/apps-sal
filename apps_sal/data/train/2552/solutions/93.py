class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        unique = set(arr)
        for i in unique:
            if arr.count(i) > len(arr) // 4:
                return i
