class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        s = set(arr)
        perc_val = 0.25 * len(arr)
        for e in s:
            if arr.count(e) > perc_val:
                return e
