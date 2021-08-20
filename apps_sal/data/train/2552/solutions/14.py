class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        sets = set(arr)
        for num in sets:
            s = arr.count(num)
            if s > len(arr) / 4:
                return num
        return None
