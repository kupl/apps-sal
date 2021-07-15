class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in arr:
            x = arr.count(i)
            perc = float(x)/float(len(arr))
            if perc > 0.25:
                return i

