class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num  = 0.25*len(arr)
        for item in arr:
            if arr.count(item)>num:
                return item
