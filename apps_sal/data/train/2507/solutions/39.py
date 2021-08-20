import collections


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for w in words:
            letters = list(set(w))
            isin = True
            for l in letters:
                if l not in chars or w.count(l) > chars.count(l):
                    isin = False
                    break
            if isin:
                count += len(w)
        return count
