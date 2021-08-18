class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        c = Counter(arr)
        for i, j in list(c.items()):
            if j == max(c.values()):
                return i
