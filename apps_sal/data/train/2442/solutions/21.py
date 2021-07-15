class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        counts, res, asc = Counter(s), [], True
        letters = sorted(set(s))
        while len(res) < len(s):
            for i in range(len(letters)):
                ch = letters[i if asc else ~i]
                if counts[ch] > 0:
                    res.append(ch)
                    counts[ch] -= 1
            asc = not asc
        return ''.join(res)

