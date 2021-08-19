class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
#         p = len(arr)*0.25
        c = Counter(arr)
#         for i,j in c.items():
#             if float(j) > p:
#                 return i
        for i, j in list(c.items()):
            if j == max(c.values()):
                return i
