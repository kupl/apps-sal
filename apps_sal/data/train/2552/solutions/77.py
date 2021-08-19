class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr)
        a = l // 4
        for i in arr:
            if arr.count(i) > a:
                return i
        return -1
