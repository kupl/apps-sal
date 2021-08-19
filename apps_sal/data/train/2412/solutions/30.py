class Solution:
    def removeDuplicates(self, S: str) -> str:
        def remove(s):
            if len(s) <= 1:
                return s
            i = 0
            s = s + '#'
            res = ''
            while i < len(s) - 1:
                if s[i] != s[i + 1]:
                    res += s[i]
                else:
                    j = i
                    while j < len(s) - 1 and s[j] == s[j + 1]:
                        j += 1
                    if (j - i) % 2 == 0:
                        res += s[j - 1]
                    i = j
                i += 1
            return res

        prev = S
        cur = remove(S)
        while cur != prev:
            prev = cur
            cur = remove(prev)

        return cur
