from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        result = []
        s = sorted(s)
        counter = Counter(s)

        while s:
            for x in sorted(set(s)):
                s.remove(x)
                result.append(x)
            for x in sorted(set(s), reverse=True):
                s.remove(x)
                result.append(x)
        return ('').join(result)
