class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        len_arr = len(arr)
        for n in set(arr):
            if arr.count(n) > len_arr * 0.25:
                return n
