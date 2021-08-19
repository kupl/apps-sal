class Solution:

    def sortString(self, s: str) -> str:
        from collections import Counter
        counts = Counter(s)
        characters = sorted(set(s))
        ch_len = len(characters)
        total = 0
        res = ''
        while total < len(s):
            for i in range(ch_len):
                ch = characters[i]
                if counts[ch] > 0:
                    res += ch
                    total += 1
                    counts[ch] -= 1
            for i in range(ch_len)[::-1]:
                ch = characters[i]
                if counts[ch] > 0:
                    res += ch
                    total += 1
                    counts[ch] -= 1
        return res
