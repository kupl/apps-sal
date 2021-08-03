class Solution:
    def sortString(self, s: str) -> str:
        res = ''
        s = list(s)
        s.sort()
        while s:
            i = 0
            curr = []
            while i < len(s):
                if s[i] not in curr:
                    curr.append(s.pop(i))
                else:
                    i += 1
            res += ''.join(curr)

            j = len(s) - 1
            curr = []
            while j >= 0:
                if s[j] not in curr:
                    curr.append(s.pop(j))
                j -= 1
            res += ''.join(curr)
        return res
