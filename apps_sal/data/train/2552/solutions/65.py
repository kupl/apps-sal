class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        elem = 0
        for ar in arr:
            if arr.count(ar) > int(0.25*len(arr)):
                elem = ar
                break
        return elem
