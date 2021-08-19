class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        return [i for i in set(arr) if arr.count(i) > len(arr) / 4][0]
