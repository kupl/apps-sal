class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        len1 = int(len(arr) * 0.25)
        count = 0
        sub = []
        for i in arr:
            if i not in sub:
                sub.append(i)
                count = 1
            else:
                count += 1
            if count > len1:
                return i
