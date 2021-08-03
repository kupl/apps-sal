class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr1 = set(arr)  # -- to remove duplicate for iteration purpose only

        cutoff = len(arr) * 0.25

        for item in arr1:
            if arr.count(item) > cutoff:
                return(item)
