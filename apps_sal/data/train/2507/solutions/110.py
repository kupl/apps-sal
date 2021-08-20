from collections import Counter


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        letters = Counter(chars)
        c = 0
        for w in words:
            if Counter(chars) & Counter(w) == Counter(w):
                c += len(w)
        return c
