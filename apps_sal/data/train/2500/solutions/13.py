class Solution:

    def maxPower(self, s: str) -> int:
        maxcount = 1
        i = 0
        while i < len(s) - 1:
            count = 1
            while i < len(s) - 1 and s[i] == s[i + 1]:
                i = i + 1
                count = count + 1
            if count > maxcount:
                maxcount = count
            if i < len(s) - 1:
                i = i + 1
        return maxcount
