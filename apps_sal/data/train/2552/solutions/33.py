class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        for (idx, val) in d.items():
            if val > len(arr) * 0.25:
                return idx
