from collections import Counter


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:

        def issubset(wc, cc):
            for x in wc.keys():
                cc[x] = cc.get(x, 0) - wc[x]
            for x in cc.keys():
                if cc[x] < 0:
                    return False
            return True
        res = 0
        cc = Counter(chars)
        for word in words:
            wc = Counter(word)
            if issubset(wc, cc.copy()):
                res += len(word)
        return res
