class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        max1 = 0
        for i in arr:
            if i in d:
                d[i] = d[i] + 1

            else:
                d[i] = 1
            max1 = max(d[i], max1)
        for i in d:
            if d[i] == max1:
                return i
