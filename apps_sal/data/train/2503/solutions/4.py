class Solution:
    def findLUSlength(self, a, b):
        if len(a) != len(b):
            return max(len(a), len(b))
        else:
            if a == b:
                return -1
            else:
                return len(a)
