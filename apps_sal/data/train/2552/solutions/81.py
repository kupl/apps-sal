class Solution:

    def findSpecialInteger(self, l: List[int]) -> int:
        for i in l:
            if l.count(i) > len(l) / 4:
                return i
